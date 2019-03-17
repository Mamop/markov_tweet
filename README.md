# markov_tweet

使い方
・twitterのAPIでキーを取得
↓
・API key、Consumer_secret、Access_token、Access_secretをメモ。コード中の'xxx'へ各自代入。
↓
・tweet_scraping.pyを実行。twitterのタイムライン最新200件分のテキストを'markov_text.txt'へスクレイピングして記入する。
この時に'@'、'#'、'https'を除外して記入させることで無駄なリプライを飛ばしたり、予期せぬリンクを踏ませるのを防ぐ。
↓
・markov_tweet.pyを実行。'markov_text.txt'にある文章をjanomeでわかち書きして'！'、'？'、'。'のいずれかがきたら一つの文章としてカウントしてツイートする。文章が長すぎた場合、文章の上限が60～91文字になるように調整する。

・現在はbotを定期実行させるためにAWSのLambdaで実行できないか色々試している。
