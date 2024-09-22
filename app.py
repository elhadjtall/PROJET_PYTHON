from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Initialiser l'application Flask
app = Flask(__name__)

# Exemple de données
def get_data():
    data = {
        'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
        'Valeur': [10, 15, 8, 12, 17, 9, 20, 18, 14, 22]
    }
    return pd.DataFrame(data)

# Route principale pour afficher le dashboard
@app.route('/')
def dashboard():
    df = get_data()

    # Création d'un graphique avec Plotly
    fig = px.line(df, x='Date', y='Valeur', title='Exemple de graphique')
    
    # Générer le graphique en HTML
    graph_html = pio.to_html(fig, full_html=False)

    # Renvoyer le template avec le graphique
    return render_template('dashboard.html', graph_html=graph_html)

# La route pour l'acceuil
@app.route('/acceuil')
def acceuil():
    return render_template('acceuil.html')

# La route pour le recrutement 
@app.route('/recrutement')
def recrutement():
    return render_template('recrutement.html')

# La route pour la page "À propos"
@app.route('/about')
def about():
    return render_template('about.html')

# Exécution de l'application
if __name__ == '__main__':
    app.run(debug=True)
