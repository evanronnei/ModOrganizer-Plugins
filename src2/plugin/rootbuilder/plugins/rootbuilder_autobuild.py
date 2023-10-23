import mobase
from pathlib import Path
from ..core.rootbuilder_plugin import RootBuilderPlugin

try:
    from PyQt5.QtCore import QCoreApplication
except:
    from PyQt6.QtCore import QCoreApplication

class RootBuilderAutobuild(RootBuilderPlugin, mobase.IPluginFileMapper):
    """Autobuild plugin, handles all the automated background parts of Root Builder."""

    def __init__(self):
        super().__init__()

    def init(self, organiser=mobase.IOrganizer):
        res = super().init(organiser)
        self._organiser.onAboutToRun(lambda appName: self.onAboutToRun(appName))
        self._organiser.onFinishedRun(lambda appName, resultCode: self.onFinishedRun(appName, resultCode))
        return res
    
    def description(self):
        return self.__tr("Handles the automated build and clear for Root Builder's autobuild mode.")
    
    def __tr(self, trstr):
        return QCoreApplication.translate(self._pluginName, trstr)

    def mappings(self):
        """Returns mappings, if there are any, for usvfs mode."""
        return self._rootBuilder.mappings()
    
    def onAboutToRun(self, appName:str) -> bool:
        """Handles automated build, if enabled."""
        # Handle if redirection is needed.
        if self._rootBuilder._settings.redirect():
            gamePath = self._rootBuilder._strings.gamePath()
            targetsGame = self._rootBuilder._paths.pathShared(gamePath, appName)
            if not targetsGame:
                modFolders = self._rootBuilder._paths.enabledRootModFolders()
                for mod in modFolders:
                    if self._rootBuilder._paths.pathShared(mod, appName):
                        relativePath = self._rootBuilder._paths.relativePath(mod, appName)
                        redirectPath = str(Path(gamePath) / relativePath)
                        self._organiser.waitForApplication(self._organiser.startApplication(redirectPath))
                        return False
    
        if self._rootBuilder._settings.autobuild():
            # Handle the automated build now.
            self._rootBuilder.build()

        return True
    
    def onFinishedRun(self, appName:str, resultCode:int):
        """Handles automated clear, if enabled."""
        if self._rootBuilder._settings.autobuild():
            self._rootBuilder.clear()
