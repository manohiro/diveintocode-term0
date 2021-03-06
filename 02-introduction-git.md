## 1.Gitとは
Gitは、プログラムのソースコードなどの変更履歴を記録・追跡するための分散型バージョン管理システムである。Linuxカーネルのソースコード管理に用いるためにリーナス・トーバルズによって開発され、それ以降ほかの多くのプロジェクトで採用されている。  
Gitでは、各ユーザのワーキングディレクトリに、全履歴を含んだリポジトリの完全な複製が作られる。したがって、ネットワークにアクセスできないなどの理由で中心リポジトリにアクセスできない環境でも、履歴の調査や変更の記録といったほとんどの作業を行うことができる。これが「分散型」と呼ばれる理由である。

### 1.1.Gitの特徴
1. ファイルの変更履歴の管理
  Gitを使えば、「◯月◯日に、◯◯さんが◯◯を変更した」という変更履歴を管理できるので、ファイル名をいちいち変更して保存しておく必要がなくなくなる。  
2. 過去のファイルの復元
     Gitを使えば、変更履歴をそれぞれ管理しているので、いつでも任意の時点のファイルに戻せる。
3. チームでの共有が可能
    ネット環境を使用すれば、同じチーム内のメンバとファイルの変更履歴などが共有できる。  
    複数人での作業を行う際に起こりがちな共通漏れ、マージミスによる上書き等の問題も回避することができる。

### 1.2.類似ソフトウェア
Gitと同様にバージョン管理システムにApache Subversion(SVN)がある。Gitとの違いはバージョン管理システムが分散型バージョン管理システムでなく、集中型バージョン管理システムであることである。

## 2.gitコマンド
### 2.1.git init
「**git init**」はリポジトリ作成を行うコマンドである。リポジトリを作成したいディレクトリでこのコマンドを実行すると.gitディレクトリが作成され、Gitリポジトリの管理ファイル等がここに作成される。  
また、同じリポジトリに対して再度実行しても、上書きされることはない。

### 2.2.git add
Gitでは、Gitの管理下に置かれた、実作業をしているディレクトリのことをワークツリーと呼ぶ。  
そして、Gitではリポジトリとワークツリーの間にはステージング領域(別名:インデックス)というものが存在している。ステージング領域とは、リポジトリにコミットする準備をするための場所のことである。  
ワークツリーのファイルをステージング領域に登録をするには  
**git add**  
コマンドで行うことができる。  
例として、hoge.htmlをステージング領域に追加・削除をコマンド方法を以下に示す。  

### hoge.htmlをステージング領域に追加
**git add hoge.html**

### hoge.htmlをステージング領域から削除（以下２つは同義）
**git reset hoge.html**  
**git reset HEAD hoge.html**  

### 2.3.git commit
「**git commit**」はステージング領域からリポジトリにファイルを登録するコマンドである。  
コミットした履歴は  
**git log**  
で確認することができる。  
直前のコミットを取り消すについては  
**git reset --soft HEAD^**  
で実行することができる。  
このコマンドのオプションの意味を以下に示す。  
- --hardオプション：コミット取り消した上でワークディレクトリの内容も書き換えたい場合に使用。
- --softオプション：ワークディレクトリの内容はそのままでコミットだけを取り消したい場合に使用。
- HEAD^：直前のコミットを意味する。
- HEAD~{n} ：n個前のコミットを意味する。

また、特定のコミットに戻したい場合は  
**git reset --soft \<commit 指定>**  
で戻したいコミットを直接指定して戻すこともできる。

### 例：commit message 1　に戻す場合
「**git log**」コマンドを実行した際に以下のログが出力され、「commit message 1」に戻す方法を示す。  

commit c4a9f6aad4ea6f5b372b9bc742c1dfc06b8641f1 (HEAD -> master, origin/master, origin/HEAD)
Author: Akihiro Nakao <nakao@diveintocode.jp>
Date:   Wed Mar 21 16:42:30 2018 +0900

    commit message 3

commit cff10b7231c5238cbd7ddab0bc19c3b7f02ba35d
Author: Akihiro Nakao <nakao@diveintocode.jp>
Date:   Wed Mar 21 16:40:31 2018 +0900

    commit message 2

commit 7b6f15fdde0f56dae4541a1a896ef6dca630e28f
Author: Akihiro Nakao <genn777f3@gmail.com>
Date:   Fri Feb 23 19:38:22 2018 +0900

    commit message 1  

### 「commit message 1」に戻すコマンド（以下２つは同義）
**git reset --soft 7b6f15fdde0f56dae4541a1a896ef6dca630e28f**  
**git reset --soft HEAD~2**