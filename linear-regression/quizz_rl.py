import random

# Preguntas con opciones y respuestas correctas
questions = [
    {
        "q": "¿Cuál es el objetivo principal de la regresión?",
        "options": [
            "Clasificar variables categóricas.",
            "Construir un modelo que permita predecir una variable dependiente a partir de variables independientes.",
            "Reducir la dimensionalidad de un conjunto de datos.",
            "Calcular probabilidades en experimentos aleatorios."
        ],
        "answer": 1
    },
    {
        "q": "Menciona un ejemplo del mundo real que puede modelarse con regresión.",
        "options": [
            "Ordenar números primos.",
            "Pronosticar la probabilidad de lluvia.",
            "Generar claves de cifrado.",
            "Contar el número de caracteres en un texto."
        ],
        "answer": 1
    },
    {
        "q": "¿Qué es el Anscombe’s quartet y por qué es importante?",
        "options": [
            "Un método de cálculo de varianza.",
            "Cuatro datasets con propiedades estadísticas iguales pero gráficos diferentes.",
            "Un algoritmo de clasificación supervisada.",
            "Una técnica de muestreo estratificado."
        ],
        "answer": 1
    },
    {
        "q": "¿Cuál es la fórmula de la media?",
        "options": [
            "x̄ = Σ xi / n",
            "x̄ = Σ xi / (n-1)",
            "x̄ = Σ xi² / n",
            "x̄ = (Σ xi)(Σ yi) / n"
        ],
        "answer": 0
    },
    {
        "q": "¿Cuál es la fórmula de la varianza muestral?",
        "options": [
            "s² = Σ (xi - x̄)² / n",
            "s² = Σ (xi - x̄)² / (n-1)",
            "s² = Σ xi² / n",
            "s² = Σ (xi - yi)² / (n-1)"
        ],
        "answer": 1
    },
    {
        "q": "¿Cuál es la fórmula de la covarianza?",
        "options": [
            "Sxy = Σ (xi - yi) / (n-1)",
            "Sxy = Σ (xi - x̄)(yi - ȳ) / (n-1)",
            "Sxy = Σ (xi - x̄)² / (n-1)",
            "Sxy = Σ xi yi / n"
        ],
        "answer": 1
    },
    {
        "q": "¿Cuál es la fórmula de la correlación?",
        "options": [
            "ρxy = Sxy / (sx * sy)",
            "ρxy = Σ xi yi / n",
            "ρxy = Σ (xi - x̄)(yi - ȳ) / n",
            "ρxy = (sx * sy) / Sxy"
        ],
        "answer": 0
    },
    {
        "q": "¿Cuál es el rango del coeficiente de correlación?",
        "options": [
            "0 ≤ ρxy ≤ 1",
            "-1 ≤ ρxy ≤ 1",
            "-∞ ≤ ρxy ≤ ∞",
            "-2 ≤ ρxy ≤ 2"
        ],
        "answer": 1
    },
    {
        "q": "¿Cuál es el modelo de regresión lineal simple?",
        "options": [
            "y = β0 + β1 x",
            "y = β0 + β1 x + β2 x²",
            "y = Σ xi / n",
            "y = ρxy + ε"
        ],
        "answer": 0
    },
    {
        "q": "¿Cómo se calculan los coeficientes β0 y β1?",
        "options": [
            "β1 = Sxy / Sxx ; β0 = ȳ - β1 x̄",
            "β1 = Σ xi yi / n ; β0 = Σ yi / n",
            "β1 = sx / sy ; β0 = 0",
            "β1 = varianza(x) ; β0 = media(y)"
        ],
        "answer": 0
    },
    {
        "q": "¿Qué representan β0 y β1?",
        "options": [
            "β0: media de x ; β1: media de y",
            "β0: ordenada en el origen ; β1: pendiente de la recta",
            "β0: desviación estándar ; β1: covarianza",
            "β0: coeficiente de determinación ; β1: correlación"
        ],
        "answer": 1
    },
    {
        "q": "¿Cuál es la fórmula del coeficiente de determinación R²?",
        "options": [
            "R² = (Sxy²) / (sx² sy²)",
            "R² = Sxy / (sx sy)",
            "R² = Σ xi² / Σ yi²",
            "R² = Σ (yi - ŷi)²"
        ],
        "answer": 0
    },
    {
        "q": "¿Cómo se interpreta un valor de R² cercano a 1?",
        "options": [
            "El modelo explica muy bien la variabilidad.",
            "El modelo explica mal la variabilidad.",
            "No existe relación lineal.",
            "Los datos tienen muchos outliers."
        ],
        "answer": 0
    },
    {
        "q": "¿Qué muestra el Dataset 3 del Anscombe’s quartet?",
        "options": [
            "Relación lineal perfecta.",
            "Un outlier que afecta el ajuste.",
            "Una relación cuadrática.",
            "Datos sin correlación."
        ],
        "answer": 1
    },
    {
        "q": "¿Qué método se usa para estimar β0 y β1?",
        "options": [
            "Máxima verosimilitud.",
            "Método de Monte Carlo.",
            "Método de mínimos cuadrados.",
            "Algoritmo de Newton-Raphson."
        ],
        "answer": 2
    }
]

def run_exam():
    print("\n📘 Examen de Regresión Lineal Simple (Opción Múltiple)\n")
    score = 0
    random.shuffle(questions)

    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['q']}")
        for idx, opt in enumerate(q["options"], 1):
            print(f"  {idx}. {opt}")
        ans = input("👉 Tu respuesta (1-4): ")
        if ans.isdigit() and int(ans)-1 == q["answer"]:
            print("✅ Correcto!\n")
            score += 1
        else:
            print(f"❌ Incorrecto. Respuesta correcta: {q['options'][q['answer']]}\n")

    print(f"🏆 Resultado final: {score}/{len(questions)} correctas.")

if __name__ == "__main__":
    run_exam()