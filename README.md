# Action Recognition Study
## 1. Introduction
이 페이지는 'Action Recognition' 연구를 위해 작성되었습니다. 소개되는 링크들은 모두 연구 목적으로만 사용되었음을 알립니다.  
This page is a collection to study 'Action Recognition'. Notice that following links are used only for study purpose. 

## 2. Data set

### 2.1 Video Surveillance
1. [i-LIDs](https://www.gov.uk/guidance/imagery-library-for-intelligent-detection-systems) : 영국 정부에서 진행 -> 현재는 [CPNI](https://www.bre.co.uk/page.jsp?id=2770)에서 test 만 진행 / 원래 데이터 자체도 유료 구매 해야함. / 현재 진행 불가
2. [i-LIDs 
2. [TRECVID_2007-9](https://www-nlpir.nist.gov/projects/trecvid/SV.2010.forms/) : 양식 작성 필요 **회신 대기중**
3. [TRECVID](https://www-nlpir.nist.gov/projects/trecvid/) 여기가 메인, 각종 컨테스트 진행 
4. [Yahoo Flickr Creative Commons 100M](https://webscope.sandbox.yahoo.com/catalog.php?datatype=i&did=67&guccounter=1) - [아마존 AWS](https://us-east-2.console.aws.amazon.com/console/home?region=us-east-2) 계정 필요. - [[paper]](https://webscope.sandbox.yahoo.com/files/W14-5406.pdf)
5. [KISA](https://www.kisa.or.kr/notice/press_View.jsp?mode=view&p_No=8&b_No=8&d_No=1497) (한국) KISA 지능형 CCTV 성능 평가 - [[안내 PDF]](https://www.kisis.or.kr/common/proc/kisis/bbs/28/fileDownLoad/1882.do) 배포용 - 시험용 - 인증용 3단계로 이루어짐: **배회 침입** 유기 쓰러짐 싸움 방화 6 카테고리 분류 (볼드체는 필수 항목) / 배포용 DB의 양이 많지 않아 실험 진행에 어려움이 많을 듯 
6. [VIRAT Video Dataset](http://www.viratdata.org/) 차량 관련 surveillance 데이터 - 왜 인지 모르겠지만 **손상된 압축파일**

### 2.2 Human Action 
1. [Kinetics-400](https://deepmind.com/research/open-source/open-source-datasets/kinetics/) - 400개 action / 10초 비디오 
2. [Moments in Time](http://moments.csail.mit.edu/) - 330개 action / 3초 비디오 80만개
3. [UCF-101](http://crcv.ucf.edu/data/UCF101.php) - 101개 action /  1)Human-Object Interaction 2) Body-Motion Only 3) Human-Human Interaction 4) Playing Musical Instruments 5) Sports. 
4. [HMDB-50](http://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/#Downloads)
5. [Youtube-BB](https://research.google.com/youtube-bb/) - [[paper]](https://arxiv.org/pdf/1702.00824)


## 3. Related Works

### 3.1 Papers - 추가 예정
1. temporal segment network - [[code]]() [[paper]]()
2. C3D - [[code]]() [[paper]]()
3. pseudo-3D residual network (P3D) - [[code]]() [[paper]]()
4. TRN - [[code]]() [[paper]]()
5. non-local neural networks]() - [[code]]() [[paper]]()
6. Inception-ResnetV2 - [[code]]() [[paper]]()
7. ARTNet - [[code]]() [[paper]]()

### 3.2 Collections
 

## 4. Progress

- 데이터 셋 조사 (~2018.07.20)
- 관련 기술 조사 (~2018.07.20)
