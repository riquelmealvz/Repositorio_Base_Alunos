import streamlit as st

def main():
    st.title("Calculadora de IMC")

    peso = st.number_input("Peso (kg)", min_value=0.1, format="%.2f")
    altura = st.number_input("Altura (m)", min_value=0.1, format="%.2f")

    if st.button("Calcular"):
        if altura > 0:
            imc = peso / (altura * altura)
            
            if imc < 18.5:
                categoria = "Magreza"
            elif imc < 25:
                categoria = "Normal"
            elif imc < 29.9:
                categoria = "sobre peso"
            elif imc < 34.9:
                categoria = "OBESIDADE GRAU 1"
            elif imc < 39.9:
                categoria = "OBESIDADE GRAU 2"
            else:
                categoria = "OBESIDADE GRAU 3"        
            
            st.write(f"IMC: {imc:.2f}")
            st.write(f"Categoria: {categoria}")
        else:
            st.error("Altura deve ser maior que zero.")

if __name__ == "__main__":
    main()

