from tkinter import *



janela = Tk()
janela.title('Paulinho MonoHTML')
janela.geometry('400x400')


txt_hour = Label(janela,text='Hour')
txt_min = Label(janela,text='Min')
txt_sec =Label(janela,text='Sec')

txt_hour2 = Label(janela,text='Hour')
txt_min2 = Label(janela,text='Min')
txt_sec2 =Label(janela,text='Sec')

texto_shut = Label(janela,text='Shutdown')
texto_shut.grid(column=0, row=0,padx=(60,0))

hour_shut = Text(janela, width=3 ,height=1)
hour_shut.place(y=30,x=40)
txt_hour.place(y= 50, x= 40)

min_shut = Text(janela, width=3 ,height=1)
min_shut.place(y=30,x=80)
txt_min.place(y= 50, x= 80)

sec_shut = Text(janela, width=3 ,height=1)
sec_shut.place(y=30,x=120)
txt_sec.place(y= 50, x= 120)


texto_click = Label(janela, text='Clicks Delay')
texto_click.grid(column=1, row=0,padx=(150,0))


hour_click = Text(janela, width=3 ,height=1)
hour_click.place(y=30,x=400-150)
txt_hour2.place(y= 50, x= 400-150)

min_click = Text(janela, width=3 ,height=1)
min_click.place(y=30,x=400-110)
txt_min2.place(y= 50, x= 400-110)

sec_click = Text(janela, width=3 ,height=1)
sec_click.place(y=30,x=400-70)
txt_sec2.place(y= 50, x= 400-70)


janela.mainloop()











#os.system('shutdown /s /t 1') #para desligar o pc
    
#while True:
 #   keyboard.wait(botao)
  #  if keyboard.is_pressed(botao):
   #     sleep(0.1)
    #    while True:
     #       pyautogui.click()
      #      print('cliquei')
       #     if keyboard.is_pressed(botao):
        #        print('parei')
         #       break



#keyboard.wait()