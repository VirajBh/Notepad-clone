import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *


class notepad(QMainWindow):
    def __init__(self):
        super(notepad,self).__init__()
        self.editor = QTextEdit()
        #to adjust font size 
        self.editor.setFontPointSize(20)
        self.setCentralWidget(self.editor)
        # to make fot size box ||||QSpinBox means the value inside the box can spin 
        self.font_size_box=QSpinBox()
        #to maximized when app is open
        self.showMaximized()
        #to add tiltle in app
        self.setWindowTitle("Notepad Clone")
        # to create toolbar
        self.create_tool_bar()
        #for menu bar
        self.create_menu_bar()

    """ to create menu bar like file, edit ,insert,etc"""
    def create_menu_bar(self):
        menu_bar=QMenuBar()
        """ ____FILE___"""
        file_menu = QMenu("File",self)
        menu_bar.addMenu(file_menu)
        # to add function in menu bar
        """ save as pdf"""
        save_as_pdf_action = QAction('save as pdf', self)
        save_as_pdf_action.triggered.connect(self.save_as_pdf)
        file_menu.addAction(save_as_pdf_action)
        

    
        """__edit___"""
        edit_menu = QMenu("Edit",self)
        menu_bar.addMenu(edit_menu)
        """ ____insert______"""
        view_menu = QMenu("View",self)
        menu_bar.addMenu(view_menu)






        self.setMenuBar(menu_bar)
        
    """ tool bar function"""
    def create_tool_bar(self):
        tool_bar=QToolBar()

        """____________UNDO_________"""
        undo_action = QAction(QIcon("undo 1.png"),'undo',self)
        undo_action.triggered.connect(self.editor.undo)
        tool_bar.addAction(undo_action)
        """ ________ REDO____"""
        redo_action = QAction(QIcon("redo.png"),'redo',self)
        redo_action.triggered.connect(self.editor.redo)
        tool_bar.addAction(redo_action)
        #to add space between undo redo and cut copy paste
        tool_bar.addSeparator()
        tool_bar.addSeparator()
        

        """ _______CUT__________"""  
        cut_action = QAction(QIcon("cut.png"),'cut',self)
        cut_action.triggered.connect(self.editor.cut)
        tool_bar.addAction(cut_action)
        """ _______COPY__________"""
        copy_action = QAction(QIcon("copy.png"),'copy',self)
        copy_action.triggered.connect(self.editor.copy)
        tool_bar.addAction(copy_action)
        """ _______Paste__________"""
        paste_action = QAction(QIcon("paste.png"),'paste',self)
        paste_action.triggered.connect(self.editor.paste)
        tool_bar.addAction(paste_action)

        tool_bar.addSeparator()
        tool_bar.addSeparator()
        
        """ font size box"""
        self.font_size_box.setValue(20)
        self.font_size_box.valueChanged.connect(self.set_font_size)
        tool_bar.addWidget(self.font_size_box)


        self.addToolBar(tool_bar)
    #font size function 
    def set_font_size(self):
        value=self.font_size_box.value()
        self.editor.setFontPointSize(value)

    def save_as_pdf(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Export PDF', None, 'PDF Files (*.pdf)')
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(file_path)
        self.editor.document().print_(printer)
    
    


app = QApplication(sys.argv)
window = notepad()
window.show()
sys.exit(app.exec_())  