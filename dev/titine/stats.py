import matplotlib.pyplot as plt

def diagramme_bande(nbEcole, nbLoisirs, nbEpiceries, nbBoutique, nbBureaux, nbRetail, nbPlex, etagesPlex, nbApparts, etagesApparts, targetPopulation):

    # Sample data
    categories = ['Ecole', 'Loisirs', 'Epicerie', 'Retail', 'Boutique', 'Bureaux', 'Plex','Apparts']
    values = [nbEcole, nbLoisirs, nbEpiceries, nbRetail, nbBoutique, nbBureaux,  nbPlex,nbApparts]

    # Create a bar chart
    plt.bar(categories, values, color='blue')

    # Add labels and title
    plt.xlabel('Type de batiment')
    plt.ylabel('Nombre')
    plt.title('Repartition des divers batiments')

    # Show the plot
    plt.show()

def pie_chart(nbEcole, nbLoisirs, nbEpiceries, nbBoutique, nbBureaux, nbRetail, nbPlex, etagesPlex, nbApparts, etagesApparts, targetPopulation):

    import matplotlib.pyplot as plt

    # Sample data
    labels = ['Résidentiel', 'Commercial', 'Communautaire']
    sizes = [nbPlex+nbApparts, nbEpiceries+nbBoutique+nbBureaux+nbRetail,nbEcole+nbLoisirs]

    # Create a pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'green', 'blue'])

    # Add a title
    plt.title('Pie Chart de la réparatition des batiments')

    # Show the plot
    plt.show()