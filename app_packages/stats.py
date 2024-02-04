import matplotlib.pyplot as plt

def diagramme_bande(nbEcole, nbLoisirs, nbEpiceries, nbBoutique, nbBureaux, nbRetail, nbPlex, etagesPlex, nbApparts, etagesApparts, nbPark):
    plt.figure()
    # Sample data
    categories = ['Ecole', 'Loisirs', 'Epicerie', 'Retail', 'Boutique', 'Parc', 'Bureau', 'Plex','Appart']
    values = [nbEcole, nbLoisirs, nbEpiceries, nbRetail, nbBoutique, nbPark, nbBureaux, nbPlex,nbApparts]

    # Create a bar chart
    colors = ['#008EE7', '#E7D900', '#8000E7', '#E76300','#E7007C', '#28E700', '#474747', '#838383', '#838383']
    plt.bar(categories, values, color=colors)

    for i, values in enumerate(values):
        plt.text(i, values + 0.5, str(values), ha='center', va='bottom')

    # Add labels and title
    plt.xlabel('Type de batiment')
    plt.ylabel('Nombre')
    plt.title('Repartition des divers batiments')

    # Show the plot
    file_path = "static/images/diagramme_bandes.png"
    plt.savefig(file_path, dpi=300, bbox_inches='tight')
    plt.show()

def pie_chart(nbEcole, nbLoisirs, nbEpiceries, nbBoutique, nbBureaux, nbRetail, nbPlex, etagesPlex, nbApparts, etagesApparts, nbPark):
    plt.figure()
    # Sample data
    labels = ['Résidentiel', 'Commercial', 'Communautaire']
    sizes = [nbPlex+nbApparts, nbEpiceries+nbBoutique+nbBureaux+nbRetail,nbEcole+nbLoisirs+nbPark]

    # Create a pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'green', 'blue'])

    # Add a title
    plt.title('Pie Chart de la réparatition des batiments')

    # Show the plot
    file_path = "static/images/pie_chart.png"
    plt.savefig(file_path, dpi=300, bbox_inches='tight')
    plt.show()

def nb_solar_pannels(nbEcole, nbLoisirs, nbEpiceries, nbBoutique, nbBureaux, nbRetail, nbPlex, etagesPlex, nbApparts, etagesApparts, targetPopulation, nbPark):

    consumption_total= 0
    consumption_total = consumption_total+ nbEcole*11*6*40*40/0.09290304 #kWh/year
    consumption_total = consumption_total+(nbPlex+nbApparts)*11*40*40/0.09290304 #kWh/year
    consumption_total = consumption_total+nbEpiceries*44.2*40*40/0.09290304 #kWh/year
    


