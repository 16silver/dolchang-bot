# Dolchang-bot
Hearthstone card Database bot (for Korean)

한국인을 위한 하스스톤 카드 DB 봇입니다.

hs.inven.co.kr에서 카드 정보를 읽어 옵니다. 필터링 등의 추가 검색 옵션은 개발 중입니다.

## Usage
### How to run
- Update dball.txt: ```> python3 dbupdate.py```
- Run a bot: ```> python3 bot.py```

### Commands
- `hs <word>`: `word`를 포함하는 카드를 모두 찾습니다. 결과가 1개라면, 그 카드의 설명을 보여줍니다. 2개 이상이라면, 해당하는 카드 list를 보여줍니다. 10개 이상이라면, list의 앞 10개만 보여줍니다.
  
- `hs <num> <word>`: `word`를 포함하는 카드 중 `num`번째 카드를 보여줍니다. minus index를 지원합니다.

- `hs + <letter>`: `letter`는 한글 글자 1개여야 합니다. `letter`로 시작하는 카드들을, 단어가 긴 순서대로 보여줍니다.

- `echo <msg>`: `msg`를 그대로 말해줍니다.

- "하스스톤"이라는 단어가 들어 있는 메시지에는, 여관주인의 대사 중 랜덤하게 하나를 골라 반응합니다.
