import matplotlib.pyplot as plt
import pandas as pd


history_e_2 = pd.read_csv(
    "D:\Studium\BA\models/histories/history_1e-2.csv")
history_e_3 = pd.read_csv(
    "D:\Studium\BA\models/histories/history_1e-3.csv")
history_cycle = pd.read_csv(
    "D:\Studium\BA\models/histories/history_cycling.csv")


def plot_acc():
    plt.plot(range(1, len(history_e_2.val_accuracy)+1),
             history_e_2.val_accuracy, color="C1", linewidth="1.3", label="1e-2")
    plt.plot(range(1, len(history_e_3.val_accuracy)+1),
             history_e_3.val_accuracy, color="C0", linewidth="1.3", label="1e-3")
    plt.plot(range(1, len(history_cycle.val_accuracy)+1),
             history_cycle.val_accuracy, color="C2", linewidth="1.3", label="cycling approach")
    plt.title('Model accuracy')
    plt.legend()
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.show()


def plot_loss():
    plt.plot(range(1, len(history_e_2.val_loss)+1),
             history_e_2.val_loss, color="C1", linewidth="1.3", label="1e-2")
    plt.plot(range(1, len(history_e_3.val_loss)+1),
             history_e_3.val_loss, color="C0", linewidth="1.3", label="1e-3")
    plt.plot(range(1, len(history_cycle.val_loss)+1),
             history_cycle.val_loss, color="C2", linewidth="1.3", label="cycling approach")
    plt.title('Model loss')
    plt.legend()
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.show()


plot_acc()
plot_loss()
