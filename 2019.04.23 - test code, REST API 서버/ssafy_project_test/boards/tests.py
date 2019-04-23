# from django.test import TestCase
from test_plus.test import TestCase
from django.conf import settings
from django.urls import reverse
from .models import Board
from .forms import BoardForm

# 1. settings test
class Settings_test(TestCase):   # settings를 테스트하며, TestCase를 인자로 넣어 테스트
    def test_01_settings(self):
        self.assertEqual(settings.USE_I18N, True)  # USE_I18N이 True인지 테스트, 같지 않으면 경고 발생
        self.assertEqual(settings.USE_TZ, False)
        self.assertEqual(settings.LANGUAGE_CODE, 'ko-kr')
        self.assertEqual(settings.TIME_ZONE, 'Asia/Seoul')

# 2. Model test
class BoardModelTest(TestCase):
    def test_01_model(self):
        board = Board.objects.create(title='test title', content='test content', user_id=1)   # board 인스턴스 만들기
        self.assertEqual(str(board), f'Board{board.pk}', msg='출력 값이 일치하지 않음')   # board의 str값이 board.pk와 같은지 확인

    def test_02_boardform(self):
        # given
        data = {'title': '제목', 'content': '내용'}
        # when + then
        self.assertEqual(BoardForm(data).is_valid(), True)
    
    def test_03_boardform_without_title(self):
        data = {'content': '내용'}
        self.assertEqual(BoardForm(data).is_valid(), False)

    def test_04_boardform_without_content(self):
        data = {'title': '내용'}
        self.assertEqual(BoardForm(data).is_valid(), False)
    

# 3. View test
class BoardViewTest(TestCase):
    def setUp(self):
        self.user = self.make_user(username='test', password='qawsedrf!')
    # create test에서의 포인트는 form을 제대로 주는가(넘기는가)에 있다
    # 가장 기본은 get_check_200
    def test_01_get_create(self):
        # user가 given 역할(유저가 무엇인가를 준다)
        # user = self.make_user(username='test', password='qawsedrf!')
        # when이 with문 역할(값을 넣거나 상태 변경)
        with self.login(username='test', password='qawsedrf!'):  # 아래에서 error가 나도 계속해서 login 유지됨
            response = self.get_check_200('boards:create')
            # then(테스트 검증)
            self.assertContains(response, '<form')   # boards의 create을 응답한 값과 form을 넘겨준 값이 같은지 확인
            self.assertIsInstance(response.context['form'], BoardForm)
    
    def test_02_get_create_login_required(self):  # 로그인이 제대로 되는가?
        self.assertLoginRequired('boards:create')  # create에서 login 필요한가?
        
    def test_03_post_create(self):
        # given = 사용자와 작성한 글 데이터
        # user = self.make_user(username='test', password='qawsedrf!')
        data = {'title': 'test title', 'content': 'test content'}  # post 방식 글쓰기
        # when = 로그인을 해서 post 요청으로 해당 url로 요청보낸 경우
        with self.login(username='test', password='qawsedrf!'):
            # then = 글이 작성되고, 페이지가 detail로 redirect 된다
            self.post('boards:create', data=data)
            # self.response_302()

    # def test_04_board_create_without_content(self):
    #     # given = content 없이 들어오는 데이터(title만 존재)
    #     data = {'title': 'test title',}
    #     # when
    #     with self.login(username='test', password='qawsedrf!'):
    #         # then
    #         response = self.post('boards:create', data=data)   # 이것에 대한 반응을 response에 넣음
    #         self.assertContains(response, '필수 항목입니다!')
    #         # form.is_valid()를 통과하지 못해서 팅겨져 나옴
            # assertContains response에 해당하는 글자가 있는지 확인하는 메소드

    # detail 페이지가 제대로 출력되는지 확인
    def test_05_detail_containes(self):  
        # given
        # board = Board.objects.create(title='제목', content='내용', user=self.user)
        board = Board.objects.create(title='제목', content='내용', user_id=1)
        # when
        self.get_check_200('boards:detail', board_pk=board.pk)  # 글이 작성될 때 잘 뜨는가?
        # then
        self.assertResponseContains(board.title, html=False)
        self.assertResponseContains(board.content, html=False)

    def test_06_detail_template(self):
        board = Board.objects.create(title='제목', content='내용', user_id=1)
        response = self.get_check_200('boards:detail', board_pk=board.pk)
        self.assertTemplateUsed(response, 'boards/detail.html')   # 실제 띄우는 템플릿이 detail.html이 맞는가?
    
    def test_07_get_index(self):   # 페이지가 잘 나오는가?
        # given when then
        self.get_check_200('boards:index')
        
    def test_08_index_template(self):   # 템플릿 사용 여부
        # when then
        response = self.get_check_200('boards:index')
        self.assertTemplateUsed(response, 'boards/index.html')   # template이 사용되고 있는가?
        
    def test_09_index_queryset(self):
        # given - 글 2개 작성
        Board.objects.create(title='제목', content='내용', user_id=1)
        Board.objects.create(title='제목', content='내용', user_id=1)
        # boards = Board.objects.all()  # 그냥 이렇게 보내면 순서가 다름
        boards = Board.objects.order_by('-pk')
        # when
        response = self.get_check_200('boards:index')
        # then
        self.assertQuerysetEqual(response.context['boards'], map(repr, boards))
        # index에서 넘겨준 boards와 여기서 만든 boards가 같은지 확인
        
    # def test_10_delete(self):
    #     board = Board.objects.create(title='제목', content='내용', user=self.user)
    #     with self.login(username='test', password='qawsedrf!'):
    #         self.get_check_200('boards:delete', board_pk=board.pk)  # GET 방식이어서 에러 발생
        
    def test_11_delete_post(self):
        board = Board.objects.create(title='제목', content='내용', user=self.user)
        with self.login(username='test', password='qawsedrf!'):
            self.post('boards:delete', board_pk=board.pk)
            self.assertEqual(Board.objects.count(), 0)
        
    def test_12_delete_redirect(self):
        board = Board.objects.create(title='제목', content='내용', user=self.user)
        with self.login(username='test', password='qawsedrf!'):
            response = self.post('boards:delete', board_pk=board.pk)
            # then
            # print(response)
            self.assertRedirects(response, reverse('boards:index'))
    
    def test_13_get_update(self):
        board = Board.objects.create(title='제목', content='내용', user=self.user)
        with self.login(username='test', password='qawsedrf!'):
            response = self.get_check_200('boards:update', board.pk)
            self.assertEqual(response.context['form'].instance.pk, board.pk)
    
    def test_14_get_update_login_required(self):
        self.assertLoginRequired('boards:update', board_pk=1)
        # 1번 유저가 로그인했을 때 update로 들어갈 수 있는가?
    
    
    
    
    
    
    
    
    
    
    
    
    
    