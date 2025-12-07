import streamlit as st
from typing import Dict, List

# 페이지 설정
st.set_page_config(
    page_title="멘토 생성기",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 커스텀 CSS 스타일
st.markdown("""
<style>
    /* 전체 배경 */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* 사이드바 숨김 */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* 제목 스타일 */
    h1 {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    
    /* 서브 제목 스타일 */
    .subtitle {
        font-size: 1.1rem;
        color: #555;
        margin-bottom: 2rem;
        font-weight: 500;
    }
    
    /* 선택 섹션 */
    .selection-section {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
    
    /* 결과 섹션 */
    .result-section {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }
    
    /* 비디오 카드 */
    .video-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        border-left: 5px solid #667eea;
    }
    
    /* 버튼 스타일 */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.7rem 2rem;
        font-size: 1rem;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        transform: translateY(-2px);
    }
    
    /* 선택 박스 스타일 */
    .stSelectbox {
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# 직업 분야별 현직자 인터뷰 영상 데이터
INTERVIEW_DATA: Dict[str, List[Dict]] = {
    "마케팅": [
        {
            "title": "마케팅 직무 이해하기 - 실무 현직자 인터뷰",
            "link": "https://www.youtube.com/embed/dQw4w9WgXcQ",
            "thumbnail": "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        },
        {
            "title": "디지털 마케팅의 현재와 미래",
            "link": "https://www.youtube.com/embed/9bZkp7q19f0",
            "thumbnail": "https://i.ytimg.com/vi/9bZkp7q19f0/maxresdefault.jpg"
        },
        {
            "title": "마케팅 분석가의 하루",
            "link": "https://www.youtube.com/embed/jNQXAC9IVRw",
            "thumbnail": "https://i.ytimg.com/vi/jNQXAC9IVRw/maxresdefault.jpg"
        }
    ],
    "제조": [
        {
            "title": "제조업 생산관리 직무 소개",
            "link": "https://www.youtube.com/embed/ZYd1oMBMSz8",
            "thumbnail": "https://i.ytimg.com/vi/ZYd1oMBMSz8/maxresdefault.jpg"
        },
        {
            "title": "스마트팩토리 시대의 제조기술자",
            "link": "https://www.youtube.com/embed/dQw4w9WgXcQ",
            "thumbnail": "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        },
        {
            "title": "품질관리(QC)의 중요성",
            "link": "https://www.youtube.com/embed/9bZkp7q19f0",
            "thumbnail": "https://i.ytimg.com/vi/9bZkp7q19f0/maxresdefault.jpg"
        }
    ],
    "행정": [
        {
            "title": "공공기관 행정 직무 가이드",
            "link": "https://www.youtube.com/embed/jNQXAC9IVRw",
            "thumbnail": "https://i.ytimg.com/vi/jNQXAC9IVRw/maxresdefault.jpg"
        },
        {
            "title": "기업 행정팀의 역할과 업무",
            "link": "https://www.youtube.com/embed/dQw4w9WgXcQ",
            "thumbnail": "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        },
        {
            "title": "인사행정 전문가로 성장하기",
            "link": "https://www.youtube.com/embed/9bZkp7q19f0",
            "thumbnail": "https://i.ytimg.com/vi/9bZkp7q19f0/maxresdefault.jpg"
        }
    ],
    "영업": [
        {
            "title": "B2B 영업의 실제 사례",
            "link": "https://www.youtube.com/embed/ZYd1oMBMSz8",
            "thumbnail": "https://i.ytimg.com/vi/ZYd1oMBMSz8/maxresdefault.jpg"
        },
        {
            "title": "영업 사원의 하루",
            "link": "https://www.youtube.com/embed/dQw4w9WgXcQ",
            "thumbnail": "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        },
        {
            "title": "고객관계관리(CRM) 활용법",
            "link": "https://www.youtube.com/embed/jNQXAC9IVRw",
            "thumbnail": "https://i.ytimg.com/vi/jNQXAC9IVRw/maxresdefault.jpg"
        }
    ],
    "기술/개발": [
        {
            "title": "소프트웨어 개발자의 일상",
            "link": "https://www.youtube.com/embed/9bZkp7q19f0",
            "thumbnail": "https://i.ytimg.com/vi/9bZkp7q19f0/maxresdefault.jpg"
        },
        {
            "title": "백엔드 개발자 커리어 가이드",
            "link": "https://www.youtube.com/embed/jNQXAC9IVRw",
            "thumbnail": "https://i.ytimg.com/vi/jNQXAC9IVRw/maxresdefault.jpg"
        },
        {
            "title": "클라우드 엔지니어링 입문",
            "link": "https://www.youtube.com/embed/dQw4w9WgXcQ",
            "thumbnail": "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        }
    ],
    "금융": [
        {
            "title": "금융기관 입사자 가이드",
            "link": "https://www.youtube.com/embed/ZYd1oMBMSz8",
            "thumbnail": "https://i.ytimg.com/vi/ZYd1oMBMSz8/maxresdefault.jpg"
        },
        {
            "title": "투자 분석가의 실무",
            "link": "https://www.youtube.com/embed/dQw4w9WgXcQ",
            "thumbnail": "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        },
        {
            "title": "리스크 관리 전문가 직무",
            "link": "https://www.youtube.com/embed/9bZkp7q19f0",
            "thumbnail": "https://i.ytimg.com/vi/9bZkp7q19f0/maxresdefault.jpg"
        }
    ],
    "의료/헬스케어": [
        {
            "title": "의료기관 간호사 인터뷰",
            "link": "https://www.youtube.com/embed/jNQXAC9IVRw",
            "thumbnail": "https://i.ytimg.com/vi/jNQXAC9IVRw/maxresdefault.jpg"
        },
        {
            "title": "보건의료 행정가의 역할",
            "link": "https://www.youtube.com/embed/dQw4w9WgXcQ",
            "thumbnail": "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        },
        {
            "title": "의료용 기술 전문가",
            "link": "https://www.youtube.com/embed/9bZkp7q19f0",
            "thumbnail": "https://i.ytimg.com/vi/9bZkp7q19f0/maxresdefault.jpg"
        }
    ],
    "교육": [
        {
            "title": "교직의 현실과 보람",
            "link": "https://www.youtube.com/embed/ZYd1oMBMSz8",
            "thumbnail": "https://i.ytimg.com/vi/ZYd1oMBMSz8/maxresdefault.jpg"
        },
        {
            "title": "교육 콘텐츠 개발자 인터뷰",
            "link": "https://www.youtube.com/embed/dQw4w9WgXcQ",
            "thumbnail": "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        },
        {
            "title": "온라인 교육 플랫폼 기획자",
            "link": "https://www.youtube.com/embed/jNQXAC9IVRw",
            "thumbnail": "https://i.ytimg.com/vi/jNQXAC9IVRw/maxresdefault.jpg"
        }
    ],
    "디자인": [
        {
            "title": "UI/UX 디자이너 직무 소개",
            "link": "https://www.youtube.com/embed/9bZkp7q19f0",
            "thumbnail": "https://i.ytimg.com/vi/9bZkp7q19f0/maxresdefault.jpg"
        },
        {
            "title": "그래픽 디자인 포트폴리오 팁",
            "link": "https://www.youtube.com/embed/jNQXAC9IVRw",
            "thumbnail": "https://i.ytimg.com/vi/jNQXAC9IVRw/maxresdefault.jpg"
        },
        {
            "title": "브랜드 아이덴티티 디자이너",
            "link": "https://www.youtube.com/embed/dQw4w9WgXcQ",
            "thumbnail": "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        }
    ],
    "법률": [
        {
            "title": "법무사의 일상과 진로",
            "link": "https://www.youtube.com/embed/ZYd1oMBMSz8",
            "thumbnail": "https://i.ytimg.com/vi/ZYd1oMBMSz8/maxresdefault.jpg"
        },
        {
            "title": "기업 법무팀 인터뷰",
            "link": "https://www.youtube.com/embed/dQw4w9WgXcQ",
            "thumbnail": "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        },
        {
            "title": "법학전문가로 성장하기",
            "link": "https://www.youtube.com/embed/9bZkp7q19f0",
            "thumbnail": "https://i.ytimg.com/vi/9bZkp7q19f0/maxresdefault.jpg"
        }
    ]
}

# 직무별 세부 정보
JOB_DETAILS: Dict[str, Dict] = {
    "마케팅": {
        "Product Manager": {
            "description": "상품 기획 및 시장 전략 수립",
            "salary": "4,500~6,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=Product+Manager"
        },
        "Digital Marketing": {
            "description": "온라인 광고 및 SNS 마케팅 전략 수립",
            "salary": "3,500~5,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=Digital+Marketing"
        },
        "마케팅 분석가": {
            "description": "데이터 기반 마케팅 효과 측정 및 분석",
            "salary": "4,000~6,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=마케팅+분석가"
        }
    },
    "제조": {
        "생산관리": {
            "description": "공장 생산 계획 및 품질 관리",
            "salary": "3,500~5,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=생산관리"
        },
        "생산기술": {
            "description": "공정 개선 및 기술 지원",
            "salary": "4,000~6,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=생산기술"
        },
        "품질관리(QC)": {
            "description": "제품 검사 및 품질 기준 유지",
            "salary": "3,200~5,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=QC"
        }
    },
    "행정": {
        "기업 행정": {
            "description": "인사, 총무, 법무 등 행정 업무",
            "salary": "3,000~5,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=행정"
        },
        "공공기관 행정": {
            "description": "공무원 및 공공기관 행정 업무",
            "salary": "3,500~5,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=공무원"
        },
        "인사담당자": {
            "description": "채용, 인사 관리 및 교육",
            "salary": "3,500~5,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=인사담당자"
        }
    },
    "영업": {
        "B2B 영업": {
            "description": "기업 대상 영업 및 계약 관리",
            "salary": "3,500~7,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=B2B+영업"
        },
        "B2C 영업": {
            "description": "개인 고객 대상 영업",
            "salary": "3,000~6,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=영업"
        },
        "Account Manager": {
            "description": "기존 고객 관계 관리 및 성장 전략",
            "salary": "4,000~6,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=Account+Manager"
        }
    },
    "기술/개발": {
        "백엔드 개발자": {
            "description": "서버 및 데이터베이스 개발",
            "salary": "4,500~8,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=백엔드"
        },
        "프론트엔드 개발자": {
            "description": "웹/앱 UI/UX 개발",
            "salary": "4,500~8,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=프론트엔드"
        },
        "클라우드 엔지니어": {
            "description": "클라우드 인프라 구축 및 관리",
            "salary": "5,000~9,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=클라우드"
        }
    },
    "금융": {
        "투자 분석가": {
            "description": "기업/주식 분석 및 투자 권고",
            "salary": "4,500~8,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=투자분석가"
        },
        "리스크 관리": {
            "description": "금융 리스크 측정 및 관리",
            "salary": "4,500~7,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=리스크+관리"
        },
        "금융 상담사": {
            "description": "고객 자산 관리 및 투자 상담",
            "salary": "3,500~6,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=금융+상담사"
        }
    },
    "의료/헬스케어": {
        "간호사": {
            "description": "환자 진료 보조 및 건강 관리",
            "salary": "3,500~4,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=간호사"
        },
        "의료 행정": {
            "description": "병원 행정 및 의무기록 관리",
            "salary": "3,000~4,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=의료+행정"
        },
        "의료 기술 전문가": {
            "description": "의료 장비 및 시스템 운영",
            "salary": "3,500~5,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=의료+기술"
        }
    },
    "교육": {
        "교사": {
            "description": "학생 교육 및 학습 관리",
            "salary": "3,500~5,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=교사"
        },
        "교육 기획자": {
            "description": "교육 프로그램 개발 및 운영",
            "salary": "3,500~5,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=교육+기획"
        },
        "에드테크 개발자": {
            "description": "온라인 교육 플랫폼 개발",
            "salary": "4,500~8,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=에드테크"
        }
    },
    "디자인": {
        "UI/UX 디자이너": {
            "description": "사용자 중심 인터페이스 설계",
            "salary": "3,500~6,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=UI+UX"
        },
        "그래픽 디자이너": {
            "description": "광고 및 마케팅 자료 디자인",
            "salary": "3,000~5,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=그래픽+디자인"
        },
        "브랜드 디자이너": {
            "description": "브랜드 아이덴티티 개발 및 관리",
            "salary": "3,500~6,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=브랜드+디자인"
        }
    },
    "법률": {
        "법무사": {
            "description": "법무 자문 및 소송 관리",
            "salary": "5,000~9,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=법무사"
        },
        "기업 법무": {
            "description": "기업 법률 자문 및 계약 관리",
            "salary": "4,500~8,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=법무"
        },
        "법률 전문가": {
            "description": "법률 자문 및 분석",
            "salary": "5,000~10,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=법률+전문가"
        }
    ]
}


# 앱 제목
st.markdown("<h1>🎬 멘토 생성기</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">현직자의 실무 경험과 실제 채용 공고로 꿈의 직업을 발견하세요</p>', unsafe_allow_html=True)
st.divider()

# 선택 섹션
with st.container():
    st.markdown('<div class="selection-section">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        selected_field = st.selectbox(
            "📌 관심 분야 선택",
            options=list(INTERVIEW_DATA.keys()),
            index=0,
            key="field_select"
        )
    
    with col2:
        available_jobs = list(JOB_DETAILS[selected_field].keys())
        selected_job = st.selectbox(
            "💼 직무 선택",
            options=available_jobs,
            key="job_select"
        )
    
    with col3:
        st.write("")  # 높이 맞추기
        recommend_button = st.button("✨ 멘토 추천 보기", use_container_width=True, key="recommend")
    
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# 추천 결과 표시
if recommend_button or "show_results" not in st.session_state:
    st.session_state.selected_field = selected_field
    st.session_state.selected_job = selected_job
    st.session_state.show_results = True

if st.session_state.get("show_results", False):
    with st.container():
        st.markdown('<div class="result-section">', unsafe_allow_html=True)
        
        current_field = st.session_state.get('selected_field', selected_field)
        current_job = st.session_state.get('selected_job', selected_job)
        
        st.markdown(f"### 🌟 '{current_field}' - '{current_job}' 멘토")
        
        # 직무 정보
        job_info = JOB_DETAILS[current_field][current_job]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("직무 설명", job_info['description'])
        with col2:
            st.metric("예상 연봉", job_info['salary'])
        with col3:
            st.markdown(f"**[채용 공고 보기]({job_info['job_url']}) 🔗**")
        
        st.markdown("---")
        st.markdown("### 📺 현직자 인터뷰")
        
        videos = INTERVIEW_DATA[current_field]
        
        # 영상 표시
        for idx, video in enumerate(videos, 1):
            st.markdown(f'<div class="video-card">', unsafe_allow_html=True)
            st.markdown(f"**{idx}. {video['title']}**")
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(video['thumbnail'], use_column_width=True)
            
            with col2:
                st.markdown(f"[🎥 YouTube에서 보기]({video['link'].replace('embed/', 'watch?v=')})")
                st.markdown(f"*3~5분 분량의 현직자 인터뷰 영상*")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
