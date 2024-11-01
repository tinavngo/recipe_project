from .models import Recipe
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import logging

def get_recipe_name(val):
    recipename = Recipe.objects.get(id=val)
    return recipename

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()

    return graph


def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    plt.clf()  # Clear previous figures to avoid overlap
    
    # Check if 'ingredients' column is in the DataFrame
    if 'ingredients' not in data.columns or data.empty:
        logging.warning("Data is empty or does not contain 'ingredients' column.")
        return None

    fig = plt.figure(figsize=(6, 3))

    # Counting the number of ingredients for each recipe
    data['no_ingredients'] = data['ingredients'].apply(lambda x: len(x.split(',')))

    try:
        if chart_type == '1':  # Match the form input with meaningful names
            plt.pie(data['no_ingredients'], labels=data['name'], autopct='%1.1f%%')
            plt.title('Pie Chart of Number of Ingredients')

        elif chart_type == '2':
            plt.bar(data['name'], data['no_ingredients'])
            plt.xlabel('Recipe Name')
            plt.ylabel('Number of Ingredients')
            plt.title('Bar Chart of Number of Ingredients')

        elif chart_type == '3':
            plt.plot(data['name'], data['no_ingredients'], marker='o')
            plt.xlabel('Recipe Name')
            plt.ylabel('Number of Ingredients')
            plt.title('Line Chart of Number of Ingredients')

        else:
            raise ValueError('Unknown chart type: {}'.format(chart_type))

        plt.tight_layout()
        chart = get_graph()
        logging.info(f"Chart generated successfully for type: {chart_type}")
        return chart

    except Exception as e:
        logging.error(f"Error generating chart: {e}")
        return None  # Return None if an error occurs
