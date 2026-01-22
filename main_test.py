"""
GitHubとCursor連携のテスト用コード
このファイルはGitHubへのコミット・プッシュの練習用です
"""

# テキスト
def greet(name: str) -> str:
    """
    挨拶メッセージを返す関数
    
    Args:
        name: 挨拶する相手の名前
        
    Returns:
        挨拶メッセージ
    """
    return f"こんにちは、{name}さん！GitHubとCursorの連携テスト中です。"

# 数値
def add_numbers(a: int, b: int) -> int:
    """
    2つの数値を足し算する関数
    
    Args:
        a: 最初の数値
        b: 2番目の数値
        
    Returns:
        2つの数値の合計
    """
    return a + b


if __name__ == "__main__":
    # テスト実行
    print(greet("開発者"))
    print(f"計算結果: {add_numbers(5, 3)}")
    print("テスト完了！GitHubにコミットしてみましょう。")
