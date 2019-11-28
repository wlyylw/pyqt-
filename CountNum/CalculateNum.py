from PyQt5 import QtWidgets
import sys
import hello

from PyQt5 import QtGui, QtWidgets
from calculate_ui import  Ui_Form

class Qt_Form(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(Qt_Form, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_pushButton)
        self.Summary = None
        self.AllText = ""
    def btn_pushButton(self):
        textContext = self.textEdit.toPlainText()
        label = self.label_2
        if textContext =="":
            label.setText("")
            pass

        else:
            summary = hello.Summary(textContext)
            summary.summary()
            Num_List = summary.get_list_word_num()
            Word_List = summary.get_list_word()
            print(Num_List)
            print(Word_List)
            for i in range(0,len(Word_List)):
                temp_str = str(Word_List[i])
                temp_num = str(Num_List[i])
                if i % 10 == 0 :
                    self.AllText+="\n   "
                    self.AllText += temp_str + ":  " + temp_num + "次     "
                else:
                    self.AllText += temp_str + ":  " + temp_num + "次     "
            max = 0
            for t in range (0,len(Word_List)):
                if Num_List[t] > max:
                    max = Num_List[t]
                    index =t
            proportion  = Num_List[index]/len(textContext)*100
            proportion = str(proportion)
            if len(proportion)>5:
                proportion = proportion[0:5]
            self.AllText+="\n\n\n\n"\
            +"出现最多的字为: " + str(Word_List[index]) + "  "+ "共出现了" + str(Num_List[index])+ "次" + "占比为" + str(proportion)+"%"

            font = QtGui.QFont()
            font.setFamily("Arial")  # 括号里可以设置成自己想要的其它字体
            font.setPointSize(12)  # 括号里的数字可以设置成自己想要的字体大小
            label.setFont(font)
            label.setText(self.AllText)
            self.AllText = ""

            summary.Clear()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = Qt_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())