
from PySide2 import QtCore, QtGui, QtWidgets
import design_mainwindow
import design_goals
import design_goal_complete
import design_remove_goal
import design_edit_goal
import design_reward

#global var_register
#global var_goals

def f_load_register():
    import pickle
    try:
        with open('saves/register.pkl','rb') as f:
            var_register = pickle.load(f)
    except:
        var_register = []
        f_save_register(var_register)
    return var_register

def f_save_register(var_register):
    import pickle
    with open('saves/register.pkl', 'wb') as f:
        pickle.dump(var_register,f)


def f_load_goals():
    import pickle
    try:
        with open('saves/goals.pkl','rb') as f:
            var_goals = pickle.load(f)
    except:
        var_goals = []
        f_save_goals(var_goals)
    return var_goals

def f_save_goals(var_goals):
    import pickle
    with open('saves/goals.pkl', 'wb') as f:
        pickle.dump(var_goals,f)


def f_load_rewards():
    import pickle
    try:
        with open('saves/rewards.pkl','rb') as f:
            var_rewards = pickle.load(f)
    except:
        var_rewards = []
        f_save_rewards(var_rewards)
    return var_rewards

def f_save_rewards(var_rewards):
    import pickle
    with open('saves/rewards.pkl', 'wb') as f:
        pickle.dump(var_rewards,f)


def f_load_points():
    import pickle
    try:
        with open('saves/points.pkl','rb') as f:
            var_points = pickle.load(f)
    except:
        var_points = 0
        f_save_points(var_points)
    return var_points

def f_save_points(var_points):
    import pickle
    with open('saves/points.pkl', 'wb') as f:
        pickle.dump(var_points,f)


class c_win_main(QtWidgets.QMainWindow,design_mainwindow.Ui_MainWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        # load Register
        var_register = f_load_register()
        var_points = f_load_points()

        self.L_Points.setText(str(var_points))

        self.B_Register.clicked.connect(self.act_b_register)
        self.B_Goals.clicked.connect(self.act_b_goals)
        self.B_Rewards.clicked.connect(self.act_b_rewards)
        self.B_Exit.clicked.connect(exit)
        self.actionGoals.triggered.connect(self.open_win_goal)
        self.actionRewards.triggered.connect(self.open_win_reward)

    def closeEvent(self,event):
        exit()

    def focusOutEvent(self,event):
        pass

    def focusInEvent(self,event):
        pass

    def open_win_goal(self):
        self.win_goals = c_win_goals()
        self.win_goals.show()

    def open_win_reward(self):
        self.win_rewards = c_win_rewards()
        self.win_rewards.show()

    def act_b_register(self):
        # actualiza el scrollarea para mostrar el registro
        self.groupBox.setTitle("Register")

        # cargamos el registro de logros
        var_register = f_load_register()
        box_layer = QtWidgets.QVBoxLayout()

        for register in var_register:
            topic = register.get('topic')
            time = register.get('time')
            description = register.get('description')
            details = register.get('details')
            points = register.get('points')
            # creamos los objetos de qt para cada suceso del registro
            qtopic = QtWidgets.QLabel(topic)
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setItalic(False)
            font.setBold(True)
            qtopic.setFont(font)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
            qtopic.setSizePolicy(sizePolicy)
            qtime = QtWidgets.QLabel(time.date().__str__()+'   '+time.time().__str__().split('.')[0])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
            qtime.setSizePolicy(sizePolicy)
            layer_1 = QtWidgets.QHBoxLayout()
            layer_1.addWidget(qtopic)
            layer_1.addWidget(qtime)
            qdescription = QtWidgets.QLabel(description)

            qdetails = QtWidgets.QTextBrowser()
            qdetails.setText(details)
            qpoints = QtWidgets.QLabel(str(points))
            layer_2 = QtWidgets.QHBoxLayout()
            spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            layer_2.addItem(spacerItem)
            layer_2.addWidget(qpoints)

            layer = QtWidgets.QVBoxLayout()
            layer.addLayout(layer_1)
            layer.addWidget(qdescription)
            layer.addWidget(qdetails)
            layer.addLayout(layer_2)
            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.HLine)
            layer.addWidget(line)

            widget_register = QtWidgets.QWidget()
            widget_register.setLayout(layer)
            box_layer.addWidget(widget_register)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        box_layer.addItem(spacerItem)
        wid = QtWidgets.QWidget()
        wid.setLayout(box_layer)
        self.scrollArea.setWidget(wid)


    def act_b_goals(self):
        # actualiza el scrollarea para mostrar las metas
        self.groupBox.setTitle("Goals")

        # cargamos los logros
        var_goals = f_load_goals()
        box_layer = QtWidgets.QVBoxLayout()

        for goal in var_goals:
            topic = goal.get('topic')
            description = goal.get('description')
            points = goal.get('points')
            id = goal.get('id')
            # creamos los objetos de qt para el objetivo
            qtopic = QtWidgets.QLabel(topic)
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setItalic(False)
            font.setBold(True)
            qtopic.setFont(font)
            qdescription = QtWidgets.QTextBrowser()
            qdescription.setText(description)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
            qdescription.setSizePolicy(sizePolicy)
            qpoints = QtWidgets.QLabel(str(points))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
            qpoints.setSizePolicy(sizePolicy)
            # los agregamos todo a un widget que colocaremos en el layer de scrollarea
            widget_goal = QtWidgets.QWidget()
            layer_1 = QtWidgets.QHBoxLayout()
            layer_2 = QtWidgets.QHBoxLayout()
            layer_1.addWidget(qdescription)
            layer_1.addWidget(qpoints)
            #############################################
            b_complete = QtWidgets.QPushButton('Complete')
            b_edit = QtWidgets.QPushButton('Edit')
            b_remove = QtWidgets.QPushButton('Remove')
            self.f_connect_button_goals(id,b_complete,b_edit,b_remove)
            #############################################
            layer_2.addWidget(b_complete)
            layer_2.addWidget(b_edit)
            layer_2.addWidget(b_remove)
            layer = QtWidgets.QVBoxLayout()
            layer.addWidget(qtopic)
            layer.addLayout(layer_1)
            layer.addLayout(layer_2)
            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.HLine)
            layer.addWidget(line)
            widget_goal.setLayout(layer)
            box_layer.addWidget(widget_goal)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        box_layer.addItem(spacerItem)
        wid = QtWidgets.QWidget()
        wid.setLayout(box_layer)
        self.scrollArea.setWidget(wid)

    def act_b_rewards(self):
        # actualiza el scrollarea para mostrar las recompensas
        self.groupBox.setTitle("Rewards")

        # cargamos las recompensas
        var_rewards = f_load_rewards()
        box_layer = QtWidgets.QVBoxLayout()

        for reward in var_rewards:
            description = reward.get('description')
            points = reward.get('points')
            id = reward.get('id')
            # creamos los objetos de qt para las recompensas
            qdescription = QtWidgets.QTextBrowser()
            qdescription.setText(description)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
            qdescription.setSizePolicy(sizePolicy)
            qpoints = QtWidgets.QLabel(str(points))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
            qpoints.setSizePolicy(sizePolicy)
            # los agregamos todo a un widget que colocaremos en el layer de scrollarea
            widget_goal = QtWidgets.QWidget()
            layer_1 = QtWidgets.QHBoxLayout()
            layer_2 = QtWidgets.QHBoxLayout()
            layer_1.addWidget(qdescription)
            layer_1.addWidget(qpoints)
            #############################################
            b_use = QtWidgets.QPushButton('Use')
            b_edit = QtWidgets.QPushButton('Edit')
            b_remove = QtWidgets.QPushButton('Remove')
            self.f_connect_button_rewards(id,b_use,b_edit,b_remove)
            #############################################
            layer_2.addWidget(b_use)
            layer_2.addWidget(b_edit)
            layer_2.addWidget(b_remove)
            layer = QtWidgets.QVBoxLayout()
            layer.addLayout(layer_1)
            layer.addLayout(layer_2)
            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.HLine)
            layer.addWidget(line)
            widget_goal.setLayout(layer)
            box_layer.addWidget(widget_goal)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        box_layer.addItem(spacerItem)

        wid = QtWidgets.QWidget()
        wid.setLayout(box_layer)
        self.scrollArea.setWidget(wid)

    def f_connect_button_rewards(self,id,b_use,b_edit,b_remove):
        b_use.clicked.connect(lambda: self.f_b_use_reward(id))
        b_edit.clicked.connect(lambda: self.f_b_edit_reward(id))
        b_remove.clicked.connect(lambda: self.f_b_remove_reward(id))

    def f_b_use_reward(self,id):
        self.reward_use = c_win_reward_use(id)
        self.reward_use.show()

    def f_b_edit_reward(self,id):
        self.reward_edit = c_win_reward_edit(id)
        self.reward_edit.show()

    def f_b_remove_reward(self,id):
        self.reward_remove = c_win_reward_remove(id)
        self.reward_remove.show()

    def f_connect_button_goals(self,id,b_complete,b_edit,b_remove):
        b_complete.clicked.connect(lambda: self.f_b_complete_goal(id))
        b_edit.clicked.connect(lambda: self.f_b_edit_goal(id))
        b_remove.clicked.connect(lambda: self.f_b_remove_goal(id))

    def f_b_complete_goal(self,id):
        # abre la ventana goal Complete
        self.goal_complete = c_win_goal_complete(id)
        self.goal_complete.show()

    def f_b_edit_goal(self,id):
        self.goal_edit=c_win_goal_edit(id)
        self.goal_edit.show()

    def f_b_remove_goal(self,id):
        self.goal_remove = c_win_goal_remove(id)
        self.goal_remove.show()

class c_win_goals(QtWidgets.QWidget,design_goals.Ui_Form):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)

        self.B_Cancel.clicked.connect(self.destroy)
        self.B_Add.clicked.connect(self.add)
        self.RB_Recurrent.clicked.connect(self.sig_Recurrent)
        self.RB_OnlyTime.clicked.connect(self.sig_OnlyTime)

    def add(self):
        var_goals = f_load_goals()
        import random
        ids = []
        for goal in var_goals:
            ids.append(goal.get('id'))
        print (ids)
        while(True):
            id = int(1000000*random.random())
            if id in ids:
                continue
            else:
                break
        print ('id ',id)
        if (self.RB_Recurrent.isChecked()):
            frecuency = 'recurrent'
        else:
            frecuency = 'onlytime'
        new_goal = {'topic':self.T_Topic.toPlainText(),
                    'description':self.T_Description.toPlainText(),
                    'points':self.SB_Points.value(),
                    'frecuency':frecuency,
                    'id':id}
        var_goals.append(new_goal)
        f_save_goals(var_goals)
        self.destroy(True)

    def sig_Recurrent(self):
        self.RB_Recurrent.setChecked(True)
        self.RB_OnlyTime.setChecked(False)

    def sig_OnlyTime(self):
        self.RB_OnlyTime.setChecked(True)
        self.RB_Recurrent.setChecked(False)

class c_win_goal_complete(QtWidgets.QWidget,design_goal_complete.Ui_Form):
    def __init__(self,id):
        super(self.__class__,self).__init__()
        self.setupUi(self)

        # se busca la meta, si no se encuentra la ventana se cierra
        var_goals = f_load_goals()
        var_found = False
        for goal in var_goals:
            if goal.get('id')==id:
                var_found = True
                break
        if not(var_found):
            print ('NO SE ENCONTRO EL ID DE LA META')
            self.destroy()
        self.goal = goal
        # colocamos los valores de la meta en el diseño de la ventana
        self.L_Topic.setText(self.goal.get('topic'))
        self.L_Points.setText(str(self.goal.get('points')))
        self.L_Description.setText(self.goal.get('description'))
        # señales de los botones
        self.B_Complete.clicked.connect(self.f_save_on_register)
        self.B_Quit.clicked.connect(self.destroy)

    def f_save_on_register(self):
        # guardamos en el registro
        var_register = f_load_register()
        from datetime import datetime
        register = {'topic':self.goal.get('topic'),
                    'description':self.goal.get('description'),
                    'details':self.TE_Details.toPlainText(),
                    'points':self.goal.get('points'),
                    'time':datetime.now()}
        var_register.append(register)
        f_save_register(var_register)
        # borramos la meta si es una meta de onlytime
        if self.goal.get('frecuency')=='onlytime':
            var_goals = f_load_goals()
            for i in range(len(var_goals)):
                if self.goal.get('id') == var_goals[i].get('id'):
                    del var_goals[i]
                    break
            f_save_goals(var_goals)

        # agregamos los puntos
        var_points = f_load_points()
        var_points = var_points + self.goal.get('points')
        f_save_points(var_points)

        self.destroy()

class c_win_goal_remove(QtWidgets.QWidget,design_remove_goal.Ui_Form):
    def __init__(self,id):
        super(self.__class__,self).__init__()
        self.setupUi(self)

        # se busca la meta, si no se encuentra la ventana se cierra
        var_goals = f_load_goals()
        var_found = False
        for goal in var_goals:
            if goal.get('id')==id:
                var_found = True
                break
        if not(var_found):
            print ('NO SE ENCONTRO EL ID DE LA META')
            self.destroy()
        self.goal = goal

        self.B_Yes.clicked.connect(self.f_yes)
        self.B_No.clicked.connect(self.f_no)

    def f_yes(self):
        var_goals = f_load_goals()
        for i in range(len(var_goals)):
            if self.goal.get('id') == var_goals[i].get('id'):
                del var_goals[i]
                break
        f_save_goals(var_goals)
        self.destroy(True)

    def f_no(self):
        self.destroy(True)

class c_win_goal_edit(QtWidgets.QWidget,design_edit_goal.Ui_Form):
    def __init__(self,id):
        super(self.__class__,self).__init__()
        self.setupUi(self)

        # se busca la meta, si no se encuentra la ventana se cierra
        var_goals = f_load_goals()
        var_found = False
        for goal in var_goals:
            if goal.get('id')==id:
                var_found = True
                break
        if not(var_found):
            print ('NO SE ENCONTRO EL ID DE LA META')
            self.destroy()
        self.goal = goal
        # se coloca informacion de la meta sin editar
        self.T_Topic.setText(self.goal.get('topic'))
        self.T_Description.setText(self.goal.get('description'))
        self.SB_Points.setValue(self.goal.get('points'))
        if (self.goal.get('frecuency')=='recurrent'):
            self.RB_Recurrent.setChecked(True)
            self.RB_OnlyTime.setChecked(False)
        elif (self.goal.get('frecuency')=='onlytime'):
            self.RB_Recurrent.setChecked(False)
            self.RB_OnlyTime.setChecked(True)
        # se conectan las señales con las funciones
        self.B_Cancel.clicked.connect(self.destroy)
        self.B_Ok.clicked.connect(self.Ok)
        self.RB_Recurrent.clicked.connect(self.sig_Recurrent)
        self.RB_OnlyTime.clicked.connect(self.sig_OnlyTime)

    def Ok(self):
        var_goals = f_load_goals()
        if (self.RB_Recurrent.isChecked()):
            frecuency = 'recurrent'
        else:
            frecuency = 'onlytime'

        for i in range(len(var_goals)):
            if self.goal.get('id')==var_goals[i].get('id'):
                var_goals[i]['topic']=self.T_Topic.toPlainText()
                var_goals[i]['description']=self.T_Description.toPlainText()
                var_goals[i]['points']=self.SB_Points.value()
                var_goals[i]['frecuency']=frecuency
                break

        f_save_goals(var_goals)
        self.destroy(True)

    def sig_Recurrent(self):
        self.RB_Recurrent.setChecked(True)
        self.RB_OnlyTime.setChecked(False)

    def sig_OnlyTime(self):
        self.RB_OnlyTime.setChecked(True)
        self.RB_Recurrent.setChecked(False)

class c_win_rewards(QtWidgets.QWidget,design_reward.Ui_Form):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)

        self.B_Add.clicked.connect(self.Add)
        self.B_Cancel.clicked.connect(self.destroy)
        self.RB_Recurrent.clicked.connect(self.sig_Recurrent)
        self.RB_OnlyTime.clicked.connect(self.sig_OnlyTime)

    def Add(self):
        var_rewards = f_load_rewards()
        import random
        ids = []
        for reward in var_rewards:
            ids.append(reward.get('id'))
        while(True):
            id = int(1000000*random.random())
            if id in ids:
                continue
            else:
                break
        if (self.RB_Recurrent.isChecked()):
            frecuency = 'recurrent'
        else:
            frecuency = 'onlytime'
        new_reward = {'description':self.T_Description.toPlainText(),
                        'points':self.SB_Points.value(),
                        'frecuency':frecuency,
                        'id':id}
        var_rewards.append(new_reward)
        f_save_rewards(var_rewards)
        self.destroy(True)

    def sig_Recurrent(self):
        self.RB_Recurrent.setChecked(True)
        self.RB_OnlyTime.setChecked(False)

    def sig_OnlyTime(self):
        self.RB_OnlyTime.setChecked(True)
        self.RB_Recurrent.setChecked(False)

class c_win_reward_remove(QtWidgets.QWidget,design_remove_goal.Ui_Form):
    def __init__(self,id):
        super(self.__class__,self).__init__()
        self.setupUi(self)

        # se busca la recompensa, si no se encuentra la ventana se cierra
        var_rewards = f_load_rewards()
        var_found = False
        for reward in var_rewards:
            if reward.get('id')==id:
                var_found = True
                break
        if not(var_found):
            print ('NO SE ENCONTRO EL ID DE LA META')
            self.destroy()
        self.reward = reward

        self.B_Yes.clicked.connect(self.f_yes)
        self.B_No.clicked.connect(self.f_no)

    def f_yes(self):
        var_rewards = f_load_rewards()
        for i in range(len(var_rewards)):
            if self.reward.get('id') == var_rewards[i].get('id'):
                del var_rewards[i]
                break
        f_save_rewards(var_rewards)
        self.destroy(True)

    def f_no(self):
        self.destroy(True)

class c_win_reward_use(QtWidgets.QWidget,design_remove_goal.Ui_Form):
    def __init__(self,id):
        super(self.__class__,self).__init__()
        self.setupUi(self)

        # se busca la recompensa, si no se encuentra la ventana se cierra
        var_rewards = f_load_rewards()
        var_found = False
        for reward in var_rewards:
            if reward.get('id')==id:
                var_found = True
                break
        if not(var_found):
            print ('NO SE ENCONTRO EL ID DE LA META')
            self.destroy()
        self.reward = reward

        self.B_Yes.clicked.connect(self.f_yes)
        self.B_No.clicked.connect(self.f_no)

    def f_yes(self):
        var_points = f_load_points()
        var_points = var_points - self.reward.get('points')
        f_save_points(var_points)
        ################################################
        ########### Guardamos en el registro ###########
        ################################################

        # borramos la recompensa si es una recompensa de onlytime
        if self.reward.get('frecuency')=='onlytime':
            var_rewards = f_load_rewards()
            for i in range(len(var_rewards)):
                if self.reward.get('id') == var_rewards[i].get('id'):
                    del var_rewards[i]
                    break
            f_save_rewards(var_rewards)

        self.destroy(True)

    def f_no(self):
        self.destroy(True)

class c_win_reward_edit(QtWidgets.QWidget,design_reward.Ui_Form):
    def __init__(self,id):
        super(self.__class__,self).__init__()
        self.setupUi(self)

        # se busca la meta, si no se encuentra la ventana se cierra
        var_rewards = f_load_rewards()
        var_found = False
        for reward in var_rewards:
            if reward.get('id')==id:
                var_found = True
                break
        if not(var_found):
            print ('NO SE ENCONTRO EL ID DE LA META')
            self.destroy()
        self.reward = reward

        # se coloca informacion de la recompensa sin editar
        self.T_Description.setText(self.reward.get('description'))
        self.SB_Points.setValue(self.reward.get('points'))
        if (self.reward.get('frecuency')=='recurrent'):
            self.RB_Recurrent.setChecked(True)
            self.RB_OnlyTime.setChecked(False)
        elif (self.reward.get('frecuency')=='onlytime'):
            self.RB_Recurrent.setChecked(False)
            self.RB_OnlyTime.setChecked(True)

        self.B_Add.setText('Ok')
        self.B_Add.clicked.connect(self.Ok)
        self.B_Cancel.clicked.connect(self.destroy)
        self.RB_Recurrent.clicked.connect(self.sig_Recurrent)
        self.RB_OnlyTime.clicked.connect(self.sig_OnlyTime)

    def Ok(self):
        var_rewards = f_load_rewards()
        if (self.RB_Recurrent.isChecked()):
            frecuency = 'recurrent'
        else:
            frecuency = 'onlytime'

        for i in range(len(var_rewards)):
            if self.reward.get('id')==var_rewards[i].get('id'):
                var_rewards[i]['description']=self.T_Description.toPlainText()
                var_rewards[i]['points']=self.SB_Points.value()
                var_rewards[i]['frecuency']=frecuency
                break

        f_save_rewards(var_rewards)
        self.destroy(True)

    def sig_Recurrent(self):
        self.RB_Recurrent.setChecked(True)
        self.RB_OnlyTime.setChecked(False)

    def sig_OnlyTime(self):
        self.RB_OnlyTime.setChecked(True)
        self.RB_Recurrent.setChecked(False)


if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = c_win_main()
    main.show()
    sys.exit(app.exec_())
