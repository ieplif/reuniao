import streamlit as st
import css
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import locale
import plotly.graph_objects as go

# Definir o locale para português do Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def format_brazilian_currency(value):
    return f"{value:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")

def main():
    st.set_page_config(layout="wide")
    css.add_custom_css()

    st.title("ASPG - 1° Semestre/2024")

    # Menu de navegação
    slide = st.sidebar.selectbox("Escolha o slide", ["Introdução", "Slide 1", "Slide 2", "Slide 3", "Slide 4", "Slide 5", "Slide 6", "Slide 7", "Conclusão"])

    # Exibir o slide selecionado
    if slide == "Introdução":
        show_introduction()
    elif slide == "Slide 1":
        show_slide_1()
    elif slide == "Slide 2":
        show_slide_2()
    elif slide == "Slide 3":
        show_slide_3()
    elif slide == "Slide 4":
        show_slide_4()
    elif slide == "Slide 5":
        show_slide_5()
    elif slide == "Slide 6":
        show_slide_6()
    elif slide == "Slide 7":
        show_slide_7()
    elif slide == "Conclusão":
        show_conclusion()
 

def show_introduction():
    st.header("Introdução")
    st.markdown("<p style='font-size:28px;'><strong>Bem-vindo à apresentação!</strong>", unsafe_allow_html=True)
    # st.image("I:\ASPG-EXERC 2024\Relatório Semestral/image.jpeg", caption="Imagem exemplo")
    

def show_slide_1():
    st.header("Receita - Fonte Própria")
    receita_arrecadada = 12890517
    receita_a_arrecadar = 12349515
    total_receita = receita_arrecadada + receita_a_arrecadar
    percentual_arrecadado = (receita_arrecadada / total_receita) * 100

    st.markdown(f"<p style='font-size:28px;'><strong>Receita arrecadada:</strong> R$ {receita_arrecadada:,.2f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:28px;'><strong>Receita a arrecadar:</strong> R$ {receita_a_arrecadar:,.2f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:28px;'><strong>Total de receita prevista:</strong> R$ {total_receita:,.2f}</p>", unsafe_allow_html=True)

    # Dados para o gráfico
    labels = ['Receita Arrecadada', 'Receita a Arrecadar']
    sizes = [receita_arrecadada, receita_a_arrecadar]
    colors = ['#ff9999','#66b3ff']
    explode = (0.1, 0)  # explode a fatia 1

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Donut
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    st.pyplot(fig1)

def show_slide_2():
    st.header("Receita - Superávit 2023")
    valor_apurado = 823451
    receita_arrecadada = 12890517  
    total_com_superavit = receita_arrecadada + valor_apurado

    st.markdown(f"<p style='font-size:28px;'><strong>Receita arrecadada:</strong> R$ {receita_arrecadada:,.2f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:28px;'><strong>Superávit apurado:</strong> R$ {valor_apurado:,.2f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:28px;'><strong>Total com superávit:</strong> R$ {total_com_superavit:,.2f}</p>", unsafe_allow_html=True)

    # Dados para o gráfico
    labels = ['Total com Superávit']
    receita_arrecadada = [receita_arrecadada]
    valor_apurado = [valor_apurado]
    bar_width = 0.2
    colors = ['#66b3ff', '#ff9999']

    fig, ax = plt.subplots()
    ax.bar(labels, valor_apurado, bar_width, bottom=receita_arrecadada, label='Superávit Apurado', color=colors[1])
    ax.bar(labels, receita_arrecadada, bar_width, label='Receita Arrecadada', color=colors[0])
    

    ax.set_ylabel('Valor (R$)')
    ax.set_title('Receita Arrecadada e Superávit Apurado')
    ax.legend()

    # Formatar o eixo y para evitar notação científica
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'R$ {x:,.0f}'))

     # Ajustar a largura da barra
    ax.set_xlim(-0.3, 0.3)

    st.pyplot(fig)

def show_slide_3():
    st.header("Despesa - Valor Empenhado")
    pessoal = 6218231
    concessionarias = 358883
    manutencao = 3708496
    despesa_obrigatoria = 2338153
    total_empenhado = pessoal + concessionarias + manutencao + despesa_obrigatoria

    st.markdown(f"<p style='font-size:28px;'><strong>Pessoal:</strong> R$ {pessoal:,.2f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:28px;'><strong>Concessionárias:</strong> R$ {concessionarias:,.2f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:28px;'><strong>Manutenção:</strong> R$ {manutencao:,.2f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:28px;'><strong>Despesas Obrigatórias:</strong> R$ {despesa_obrigatoria:,.2f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:28px;'><strong>Total Empenhado:</strong> R$ {total_empenhado:,.2f}</p>", unsafe_allow_html=True)

     # Dados para o gráfico de pizza
    categorias = ['Pessoal', 'Concessionárias', 'Manutenção', 'Despesa Obrigatória']
    valores = [6218231, 358883, 3708496, 2338153]
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

    # Configurar as fatias do gráfico de pizza para serem distanciadas
    pull = [0.00, 0.00, 0.00, 0.00]

    # Criar o gráfico de pizza com Plotly
    fig = go.Figure(data=[go.Pie(labels=categorias, values=valores, pull=pull, textinfo='label+percent', marker=dict(colors=colors))])

    # Personalizar o layout do gráfico
    fig.update_layout(
        title_text='Distribuição das Despesas',
        title_font_size=20,
        margin=dict(t=50, b=0, l=0, r=0),
        height=1000,  # Ajustar a altura do gráfico
        uniformtext_minsize=12,  # Ajustar o tamanho mínimo do texto
        uniformtext_mode='hide',  # Ocultar texto pequeno
        showlegend=False,  # Ocultar a legenda
        annotations=[dict(text='Distribuição das Despesas', x=0.5, y=0.5, font_size=20, showarrow=False)]  # Centralizar o título
    )

    # Centralizar o gráfico
    fig.update_traces(hole=0.4, hoverinfo="label+percent+name", textfont_size=18, textposition='inside', marker=dict(line=dict(color='#000000', width=2)), pull=pull)

    # Exibir o gráfico de pizza no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def show_slide_4():
    st.header("Balanço Orçamentário: Arrecadado x Empenhado")

    valor_apurado = 823451
    receita_arrecadada = 12890517  
    total_com_superavit = receita_arrecadada + valor_apurado
    pessoal = 6218231
    concessionarias = 358883
    manutencao = 3708496
    despesa_obrigatoria = 2338153
    total_empenhado = pessoal + concessionarias + manutencao + despesa_obrigatoria
    diferenca = total_com_superavit - total_empenhado

    st.markdown(f"<p style='font-size:28px;'><strong>Total Arrecadado + Superávit</strong> R$ {total_com_superavit:,.2f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:28px;'><strong>Total Empenhado:</strong> R$ {total_empenhado:,.2f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:28px;'><strong>Diferença:</strong> R$ {diferenca:,.2f}</p>", unsafe_allow_html=True)

    # Configuração do gráfico de barras
    fig = go.Figure()

    # Adicionar a barra total_com_superavit dividida em dois segmentos
    fig.add_trace(go.Bar(
        name='Receita Arrecadada',
        x=['Total com Superávit'],
        y=[receita_arrecadada],
        marker_color='blue'
    ))

    fig.add_trace(go.Bar(
        name='Superávit',
        x=['Total com Superávit'],
        y=[valor_apurado],
        marker_color='lightblue',
        base=[receita_arrecadada]
    ))

    # Adicionar a barra total_empenhado
    fig.add_trace(go.Bar(
        name='Total Empenhado',
        x=['Total Empenhado'],
        y=[total_empenhado],
        marker_color='red'
    ))

    # Personalizar o layout do gráfico
    fig.update_layout(
        title_text='Comparação entre Total com Superávit e Total Empenhado',
        title_font_size=20,
        barmode='stack',
        height=600,  # Ajustar a altura do gráfico
        yaxis=dict(
            title='Valor',
            tickformat=',.2f',
        ),
        xaxis=dict(
            title=''
        ),
        showlegend=True
    )

    # Exibir o gráfico de barras no Streamlit
    st.plotly_chart(fig, use_container_width=True)    


def show_slide_5():
    st.header("Despesas - Casos Especiais")

     # Criar duas colunas
    col1, col2 = st.columns(2)

    # Dados para as tabelas nas duas colunas
    dados_tabela_1 = {
        "Descrição": ["Tesouro", "Tesouro*", "CEDAE"],
        "Valor": [919666, 517700, 100156]
    }
    dados_tabela_2 = {
        "Descrição": ["Acordo TGMC", "Acordo TGMC", "Não houve"],
        "Valor": [910723, 200000, 0]
    }

    # Converter os dados em DataFrames
    df_tabela_1 = pd.DataFrame(dados_tabela_1)
    df_tabela_1['Valor'] = df_tabela_1['Valor'].apply(format_brazilian_currency)

    df_tabela_2 = pd.DataFrame(dados_tabela_2)
    df_tabela_2['Valor'] = df_tabela_2['Valor'].apply(format_brazilian_currency)

    # CSS para remover as bordas das tabelas
    hide_table_row_index = """
        <style>
        tbody th {display:none}
        .blank {display:none}
        table {
            border-collapse: collapse;
            border: none;
        }
        th, td {
            border: none !important;
            padding: 8px;
            text-align: left;
        }
        </style>
    """

    # Adicionar CSS personalizado
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    # Tabela na primeira coluna
    with col1:
        st.subheader("Fonte de Recurso")
        st.markdown(df_tabela_1.to_html(index=False), unsafe_allow_html=True)

    # Tabela na segunda coluna
    with col2:
        st.subheader("Despesa")
        st.markdown(df_tabela_2.to_html(index=False), unsafe_allow_html=True)
        
    st.text("* os valores da segunda linha referente ao Tesouro estão separado por estarem disponíveis para despesa de desapropriação")

def show_slide_6():
    st.header('Previsão Orçamento 2024')

    valor_apurado = 823451
    receita_prevista = 25340032
    empenhos = 25725587
    total_receita = valor_apurado + receita_prevista
    diferenca = total_receita - empenhos

    st.markdown(f"<p style='font-size:28px;'><strong>Total Receita Prevista + Superávit:</strong> R$ {total_receita:,.2f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:28px;'><strong>Total Empenhos Estimados:</strong> R$ {empenhos:,.2f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:28px;'><strong>Diferença:</strong> R$ {diferenca:,.2f}</p>", unsafe_allow_html=True)

    # Configuração do gráfico de barras
    fig = go.Figure()

    # Adicionar a barra total_com_superavit dividida em dois segmentos
    fig.add_trace(go.Bar(
        name='Total Receita Prevista',
        x=['Total com Superávit'],
        y=[receita_prevista],
        marker_color='blue'
    ))

    fig.add_trace(go.Bar(
        name='Superávit',
        x=['Total com Superávit'],
        y=[valor_apurado],
        marker_color='lightblue',
        base=[receita_prevista]
    ))

    # Adicionar a barra total_empenhado
    fig.add_trace(go.Bar(
        name='Total Empenhos Estimados',
        x=['Total Empenhos Estimados'],
        y=[empenhos],
        marker_color='red'
    ))

    # Personalizar o layout do gráfico
    fig.update_layout(
        title_text='Comparação entre Total de Receitas previstas com Superávit e Total Empenhos Estimados',
        title_font_size=20,
        barmode='stack',
        height=600,  # Ajustar a altura do gráfico
        yaxis=dict(
            title='Valor',
            tickformat=',.2f',
        ),
        xaxis=dict(
            title=''
        ),
        showlegend=True
    )

    # Exibir o gráfico de barras no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def show_slide_7():
    st.header("Oportunidades de Melhorias")

    st.markdown("""
        
     <p style='font-size:28px;'><strong>➡️ Desenvolver uma Aplicação Web</strong>
         <p style='font-size:23px;'>📌 Controle de usuários, banco de dados, backend, frontend, build e deploy
         <p style='font-size:23px;'>📌 Painéis (Dashboards)

     <p style='font-size:28px;'><strong>➡️ IA Generavita:</strong>
         <p style='font-size:23px;'>📌 Configuração do LangChain: Integrar LangChain na aplicação Streamlit para permitir o processamento de texto e a geração de conteúdo.
         <p style='font-size:23px;'>📌 Visualização de Resultados: Exibir os resultados gerados pelos modelos LangChain diretamente na interface Streamlit.
         <p style='font-size:23px;'>📌 Interatividade: Permitir que os usuários insiram texto ou parâmetros e vejam os resultados em tempo real, ajustando dinamicamente a saída do modelo.
         <p style='font-size:23px;'>📌 RAG (Retrieval-Augmented Generation): Configurar a aplicação para buscar informações relevantes em bases de dados específicas.
         <p style='font-size:23px;'>📌 Geração de Respostas: Usar os dados recuperados para gerar respostas contextualizadas, exibindo tanto as informações recuperadas quanto o texto gerado na interface Streamlit.
         <p style='font-size:23px;'>📌 Agentes são entidades que podem realizar tarefas de forma autônoma, seguindo um conjunto de regras ou utilizando aprendizado de máquina para tomar decisões.
         <p style='font-size:23px;'>📌 Automação de Tarefas, Interação em Tempo Real, Monitoramento e Ajuste
    """, unsafe_allow_html=True)
    
def show_conclusion():
    st.header("Conclusão")
    st.markdown("<p style='font-size:24px;'><strong>Obrigado por assistir a apresentação!</strong>", unsafe_allow_html=True)



if __name__ == "__main__":
    main()
