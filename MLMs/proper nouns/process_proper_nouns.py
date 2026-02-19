import pandas as pd # type: ignore

def process_nombres_por_edad_media():

    # male
    males_read = pd.read_excel('nombres_por_edad_media.xlsx', sheet_name = "Hombres", skiprows = 6)
    males_filtered = pd.DataFrame({
        'Name': males_read['Nombre'],
        'Gender': 'male'
    })

    # female
    females_read = pd.read_excel('nombres_por_edad_media.xlsx', sheet_name = "Mujeres", skiprows = 6)
    females_filtered = pd.DataFrame({
        'Name': females_read['Nombre'],
        'Gender': 'female'
    })

    # combined
    combined = pd.concat([males_filtered, females_filtered], ignore_index = True)
    combined.to_csv('proper_nouns_ES.csv', index = False, encoding = 'utf-8')

def process_popular_baby_names():

    baby = pd.read_excel('popular_baby_names.xlsx', skiprows = 1)

    # male
    males = pd.DataFrame({
        'Name': baby['Male name'],
        'Gender': 'male'
    })

    # female
    females = pd.DataFrame({
        'Name': baby['Female name'],
        'Gender': 'female'
    })

    # combined
    combined = pd.concat([males, females], ignore_index = True)
    combined.to_csv('proper_nouns_EN.csv', index = False, encoding = 'utf-8')

if __name__ == "__main__":
    process_nombres_por_edad_media()
    process_popular_baby_names()