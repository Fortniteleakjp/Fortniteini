import os

# 対象フォルダ
target_folder = "."

print("=== .locresファイル削除処理を開始します ===")

try:
    for root, dirs, files in os.walk(target_folder):
        print(f"フォルダ確認中: {root}")

        for file in files:
            print(f"ファイル確認: {file}")

            # .locresで終わるファイルを判定
            if file.endswith(".locres"):
                file_path = os.path.join(root, file)
                print(f".locresファイルを発見: {file_path}")

                try:
                    os.remove(file_path)
                    print(f"削除成功: {file_path}")
                except Exception as e:
                    print(f"削除失敗: {file_path} エラー: {e}")

    print("=== 処理完了 ===")

except Exception as e:
    print(f"エラーが発生しました: {e}")