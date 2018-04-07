# combine-word-listening
将Merriam Webster's Vocabulary Builder的单词，通过扇贝网的音源组合成适合听写的mp3文件。

## 文件
`./list/` 文件夹：含中文释义的单词列表<br>
`blank.mp3` ：5秒空白音频文件<br>
`combine.py` ： 文件夹内所有文件合成一个文件（加入空白及结束音）<br>
`python_reading_file.py`：根据单词列表下载相关读音文件

## 进度
**现在已完成**<br>
Unit 1-10的合成。

**已知问题：**<br>
Unit2 Delphic - 改为小写 <br>
Unit3 british thermal unit - 无发音文件<br>
Unit4 Procrustean	- 改为小写<br>
Unit5 corpus delicti - 无发音 - 已解决<br>
Unit7 vis a vis, Achilles heel, Arcadia - 无发音 - 已解决<br>
Unit8 aeolian harp - 无发音 - 已解决<br>
Unit10 Sisyphean - 改小写<br>

## 版权声明及参考文献

扇贝单词书 Merriam Webster's Vocabulary Builder
[https://www.shanbay.com/wordbook/88768/]()<br>
上传者： VLane_so

扇贝音源 
版权由扇贝所有
音源API：
[http://media.shanbay.com/audio/us/%s.mp3]()
[http://media.shanbay.com/audio/uk/%s.mp3]()
Google Definition

Python音频合并
[https://blog.csdn.net/skywalkervvv/article/details/41685687]()
[https://github.com/jiaaro/pydub]()
