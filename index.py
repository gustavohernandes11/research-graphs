import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

labels = {
    "id": "ID",
    "age": "Idade (em anos)",
    "course": "Curso",
    "yearOfGraduation": "Ano da graduação (em anos)",
    "studyHours": "Horas de estudo semanais"
}

# load data
data = pd.read_csv(
    "data.csv",
    header=None,
    names=[
        labels["id"],
        labels["age"],
        labels["course"],
        labels["yearOfGraduation"],
        labels["studyHours"]
    ]
)

# descritive statistics
print(data.info())
print(data.describe())

# study hours distribuition
sns.histplot(data[labels["studyHours"]], bins=20, kde=True)
plt.title("Distribuição de horas de estudo por semana")
plt.savefig("graphs/distribuição-horas-de-estudo.png")
plt.show()

# relation between year of graduation and hours of study per week
sns.countplot(x=labels["yearOfGraduation"], hue=labels["studyHours"], data=data)
plt.title("Relação entre ano da graduação e horas de estudo por semana")
plt.savefig("graphs/relacao-ano-de-graduacao-e-horas-de-estudos.png")
plt.show()

# relation between age and hours of study per week
sns.countplot(x=labels["age"], hue=labels["studyHours"], data=data)
plt.title("Relação entre idade e horas de estudo por semana")
plt.savefig("graphs/relacao-idade-e-horas-de-estudos.png")
plt.show()
