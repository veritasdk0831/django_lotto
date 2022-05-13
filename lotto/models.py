from django.db import models
from django.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model):
    name = models.CharField(max_length=24) # 로또 번호 리스트의 이름
    text = models.CharField(max_length=255) # 로또 번호 리스트에 대한 설명
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]') # 로또 번호들이 담길 str
    num_lotto = models.IntegerField(default=5) # 6개 번호 set의 갯수
    update_date = models.DateTimeField()

    def generate(self): # 로또 번호를 자동으로 생성
        self.lottos = "" # 초기화
        origin = list(range(1,46)) # 1~45의 숫자 리스트 (range 함수에서 끝 번호는 미만의 의미이니까!)
        # 6개 번호 set 갯수만큼 1~45 뒤섞은 후 앞의 6개 골라내어 sorting
        for _ in range(0, self.num_lotto):
            random.shuffle(origin) # shuffle = 섞다~! 섞어주고~!
            guess = origin[:6] # 섞인 상태에서 6개 숫자 꺼내서
            guess.sort() # sorting 하는 것!
            self.lottos += str(guess) +'\n' # 로또 번호 str에 6개 번호 set 추가
        self.update_date = timezone.now()
        self.save() # GuessNumbers object를 DB에 저장 #DB의 commit이라고 생각하면 됨. (save = commit)

    def __str__(self): # Admin page에서 display되는 텍스트에 대한 변경
        return "pk {} : {} - {}".format(self.pk, self.name, self.text) # pk는 자동생성됨 (pk=id열=primary key -> self.pk / self.id 똑같은 말임.)