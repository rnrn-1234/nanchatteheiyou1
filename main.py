import pandas as pd
import streamlit as st 
import streamlit_wordcloud as wordcloud


def main():

    st.set_page_config(layout="centered")

    ## タイトル
    st.title('なんちゃって併用分析')

    rec = st.sidebar.radio(
        "表示件数を選択してください",
        ('30','50','100')
    )

    color = st.sidebar.radio(
        "色を選択してください",
        ('viridis','plasma','twilight','spring','summer','autumn','winter',)
    )

    layout = st.sidebar.radio(
        "レイアウトを選択してください（よくわからない）",
        ('rectangular','archimedean')
    )

    input_name = st.text_input('ブランド名を入力してください','')

    if input_name :

        if input_name == "ロキソニン":
            df = pd.read_csv(f'target_top{rec}.csv')

            # カラム名変更
            df_new = df.rename(columns={'ブランド名称': 'text', '患者数': 'value'})

            # wordcloud用データセット
            # dataframeの中身を辞書型に変更（リストの中身が辞書型）
            words = df_new.to_dict('records')

            return_obj = wordcloud.visualize(words, tooltip_data_fields={
                'text':'Bland', 'value':'#pts'
            }, per_word_coloring=False, padding=0.1, palette=f'{color}', layout=f'{layout}')

            st.table(df)

        else:
            st.error('すみません。ロキソニン以外データがありません')
    else:
        st.balloons()
    

if __name__ == '__main__':
    main()
