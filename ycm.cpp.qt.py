# NOTE Things I marked as TODO is not nessessary means I
#      will do it myself someday. It could be a suggestion
#      for anyone interested in it.

# NOTE for Linux user
# Qt common flags
# The Qt pkg-config module in Gentoo is Qt4/Qt5, But in OS X it's splited into many sub-modules.
# Do the compatible work yourself if needed
QtModules = ["QtCLucene", "QtDeclarative", "QtDesignerComponents", "QtHelp", "QtNetwork", "QtScript", "QtSql", "QtTest", "QtUiTools_debug", "QtXml",
             "QtCore", "QtDesigner", "QtGui", "QtMultimedia", "QtOpenGL", "QtScriptTools", "QtSvg", "QtUiTools", "QtWebKit", "QtXmlPatterns"]

from subprocess import Popen
from subprocess import PIPE
qtflags = []
for module in QtModules:
    qtflags += Popen(['pkg-config', '--cflags'] + QtModules, stdout=PIPE).communicate()[0].split()

flags += qtflags
