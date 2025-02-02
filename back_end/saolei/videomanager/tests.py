from django.test import TestCase
from userprofile.models import UserProfile
from .models import VideoModel, ExpandVideoModel

# Create your tests here.

class VideoManagerTestCase(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create(username='setUp', email='setUp@test.com')

    def test_zero_time(self):
        expandvideo = ExpandVideoModel.objects.create(identifier='test', cl_s=0, stnb=0, rqp=0, ioe=1, thrp=1, corr=1, ce_s=0)
        video = VideoModel.objects.create(player=self.user, file='test.evf', video=expandvideo, state='a', software='e', level='b', mode='00', timems=0, bv=1, left=1, right=0, double=0, path=0, flag=0, left_ce=1, right_ce=0, double_ce=0, op=1, isl=0, cell0=0, cell1=0, cell2=0, cell3=0, cell4=0, cell5=0, cell6=0, cell7=0, cell8=0)
        self.assertEqual(video.bvs, 0)
        self.assertEqual(video.flag_s, 0)
        self.assertEqual(video.left_s, 0)
        self.assertEqual(video.right_s, 0)
        self.assertEqual(video.double_s, 0)
        self.assertEqual(video.left_ces, 0)
        self.assertEqual(video.right_ces, 0)
        self.assertEqual(video.double_ces, 0)
        self.assertEqual(video.ce, 1)
        self.assertEqual(video.cl, 1)