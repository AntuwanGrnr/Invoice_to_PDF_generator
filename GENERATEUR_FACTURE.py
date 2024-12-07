import tkinter as tk
import jinja2
import pdfkit
##------------------CUSTOM FUNCTION---------------------------------

def export_userInput():
    facture_numero = factureNumero_byUser.get()
    facture_numero_formate = "F00"+facture_numero
    
    facture_date = factureDate_byUser.get()
    client_nom_prenom = (nomclient_byUser.get()).upper()
    client_adresse_rue = adresse_rue_byUser.get()
    client_adresse_ville = adresse_ville_byUser.get()
    facture_prestation = prestation_byUser.get()
    facture_prix = prix_byUser.get()
    
    context = {"facture_numero_formate":facture_numero_formate,"facture_date":facture_date, "client_nom_prenom":client_nom_prenom,"client_adresse_rue":client_adresse_rue,"client_adresse_ville":client_adresse_ville ,"facture_prestation":facture_prestation,
"facture_prix":facture_prix}
    
    template_loader = jinja2.FileSystemLoader("./")
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template("facture aly html forma -SIMPLE.html")
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe" )
    pdfkit.from_string(output_text, 'Aly&Co_FACTURE'+facture_numero_formate+'_'+client_nom_prenom+'.pdf', configuration = config)

    ##root.mainloop()
    
##---------------------ACCUEIL------------------------------

    
main_tkinter_window = tk.Tk()
main_tkinter_window.title("Generateur Facture PDF")
main_tkinter_window.resizable(False, False)
main_tkinter_window.geometry("400x400")

main_tkinter_window.iconbitmap('openscissors.ico')

label_greeting = tk.Label (text = "Bienvenue Alyssia", bg = "pink", font= ('Times New Roman', 20))
label_greeting.pack(pady = 15)

##----------------------CONTENU-----------------------------
label_facture_numero = tk.Label(text = "Numéro de Facture:")
label_facture_numero.pack()
factureNumero_byUser = tk.Entry (width=20)
factureNumero_byUser.pack()

label_facture_date = tk.Label(text = "Date de facture: ")
label_facture_date.pack()
factureDate_byUser = tk.Entry (width=20)
factureDate_byUser.pack()

label_nomclient = tk.Label(text = "Nom Prénom client: ")
label_nomclient.pack()
nomclient_byUser = tk.Entry (width=20)
nomclient_byUser.pack()

label_adresse_rue = tk.Label(text = "Adresse client (rue): ")
label_adresse_rue.pack()
adresse_rue_byUser = tk.Entry (width=40)
adresse_rue_byUser.pack()

label_adresse_ville = tk.Label(text = "Adresse client (code + ville): ")
label_adresse_ville.pack()
adresse_ville_byUser = tk.Entry (width=40)
adresse_ville_byUser.pack()

label_prestation = tk.Label(text = "Prestation: ")
label_prestation.pack()
prestation_byUser = tk.Entry (width=40)
prestation_byUser.pack()    

label_prix = tk.Label(text = "Prix total: ")
label_prix.pack()
prix_byUser = tk.Entry (width=20)
prix_byUser.pack()



export_button = tk.Button ( text = "Créer Facture", command = export_userInput, fg = 'white', bg = '#aeb6bf')
export_button.pack(pady=10)


tk.mainloop()

##-------------------------------------------------------------------------



