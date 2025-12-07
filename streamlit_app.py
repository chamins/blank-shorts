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
    
    /* 작은 텍스트 */
    .small-text {
        font-size: 0.9rem;
        color: #666;
        line-height: 1.6;
    }
    
    /* 직무 정보 카드 */
    .job-info-box {
        background: linear-gradient(135deg, #f0f4ff 0%, #f5f0ff 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        border-left: 5px solid #667eea;
    }
    
    /* 채용공고 링크 박스 */
    .job-link-box {
        background: linear-gradient(135deg, #fff0f5 0%, #ffe4f0 100%);
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        border-left: 5px solid #e85b8a;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# 채용공고 예시 데이터
JOB_POSTINGS = {
    "마케팅": {
        "Product Manager": [
            {"title": "Product Manager (SaaS)", "company": "Naver", "location": "서울시 강남구"},
            {"title": "Product Manager", "company": "Coupang", "location": "서울시 강남구"},
            {"title": "Senior Product Manager", "company": "Kakao", "location": "제주시 애월읍"},
            {"title": "Product Manager (B2B)", "company": "Woowa Bros", "location": "서울시 강남구"},
            {"title": "Product Manager", "company": "당근마켓", "location": "서울시 강남구"}
        ],
        "Digital Marketing": [
            {"title": "디지털 마케터", "company": "직방", "location": "서울시 중구"},
            {"title": "Performance Marketing 담당자", "company": "버킷플레이스", "location": "서울시 강남구"},
            {"title": "SNS 마케터", "company": "쿠팡", "location": "서울시 강남구"},
            {"title": "Digital Marketing Manager", "company": "삼성전자", "location": "서울시 강남구"},
            {"title": "마케팅 담당자", "company": "하이퍼커넥트", "location": "서울시 강남구"}
        ],
        "마케팅 분석가": [
            {"title": "마케팅 분석가", "company": "우아한형제들", "location": "서울시 강남구"},
            {"title": "데이터 분석가 (마케팅)", "company": "당근마켓", "location": "서울시 강남구"},
            {"title": "Growth Analytics 담당자", "company": "야놀자", "location": "서울시 강남구"},
            {"title": "마케팅 분석 전문가", "company": "스포카", "location": "서울시 강남구"},
            {"title": "분석 엔지니어", "company": "숨고", "location": "서울시 강남구"}
        ]
    },
    "제조": {
        "생산관리": [
            {"title": "생산관리 담당자", "company": "현대자동차", "location": "울산시 남구"},
            {"title": "생산계획팀", "company": "삼성전자", "location": "경주시 중심지"},
            {"title": "생산관리사", "company": "LG전자", "location": "서울시 강서구"},
            {"title": "공정관리 담당자", "company": "SK하이닉스", "location": "이천시 부발읍"},
            {"title": "생산관리 전문가", "company": "현대기아차", "location": "광주광역시"}
        ],
        "생산기술": [
            {"title": "공정기술 엔지니어", "company": "삼성전자", "location": "경주시"},
            {"title": "생산기술 담당자", "company": "현대자동차", "location": "울산시 남구"},
            {"title": "설비 엔지니어", "company": "SK하이닉스", "location": "이천시"},
            {"title": "공정개선 담당자", "company": "LG화학", "location": "여수시"},
            {"title": "기술 지원팀", "company": "포스코", "location": "포항시 남구"}
        ],
        "품질관리(QC)": [
            {"title": "품질관리 담당자", "company": "삼성전자", "location": "경주시"},
            {"title": "QC 엔지니어", "company": "현대자동차", "location": "울산시"},
            {"title": "품질보증 담당자", "company": "LG전자", "location": "서울시"},
            {"title": "검사원", "company": "SK하이닉스", "location": "이천시"},
            {"title": "품질관리 전문가", "company": "한국전력", "location": "대전시"}
        ]
    },
    "행정": {
        "기업 행정": [
            {"title": "행정담당자", "company": "삼성그룹", "location": "서울시 강남구"},
            {"title": "총무팀", "company": "LG그룹", "location": "서울시 여의도"},
            {"title": "행정관리사", "company": "SK그룹", "location": "서울시 중심지"},
            {"title": "기업 행정가", "company": "현대그룹", "location": "서울시 강남구"},
            {"title": "행정 담당자", "company": "포스코", "location": "포항시"}
        ],
        "공공기관 행정": [
            {"title": "행정직 공무원", "company": "대한민국 정부", "location": "서울시"},
            {"title": "공공기관 행정가", "company": "한국철도공사", "location": "대전시"},
            {"title": "행정 전문가", "company": "한국전력", "location": "대전시"},
            {"title": "행정직", "company": "기획재정부", "location": "서울시"},
            {"title": "행정 담당자", "company": "서울시청", "location": "서울시 중구"}
        ],
        "인사담당자": [
            {"title": "인사담당자", "company": "삼성전자", "location": "서울시 강남구"},
            {"title": "HR 담당자", "company": "LG전자", "location": "서울시 강서구"},
            {"title": "인사관리사", "company": "현대자동차", "location": "울산시"},
            {"title": "인사팀", "company": "SK하이닉스", "location": "이천시"},
            {"title": "채용담당자", "company": "쿠팡", "location": "서울시 강남구"}
        ]
    },
    "영업": {
        "B2B 영업": [
            {"title": "B2B 영업사원", "company": "쿠팡", "location": "서울시 강남구"},
            {"title": "기업영업 담당자", "company": "우아한형제들", "location": "서울시 강남구"},
            {"title": "B2B 세일즈", "company": "직방", "location": "서울시 중구"},
            {"title": "엔터프라이즈 세일즈", "company": "토스", "location": "서울시 강남구"},
            {"title": "기업영업가", "company": "당근마켓", "location": "서울시 강남구"}
        ],
        "B2C 영업": [
            {"title": "영업사원", "company": "삼성전자", "location": "서울시 강남구"},
            {"title": "매장 매니저", "company": "롯데백화점", "location": "서울시 중구"},
            {"title": "판매원", "company": "현대자동차", "location": "서울시 강남구"},
            {"title": "영업 담당자", "company": "LG전자", "location": "서울시 강서구"},
            {"title": "영업 전사", "company": "한샘", "location": "서울시 강동구"}
        ],
        "Account Manager": [
            {"title": "Account Manager", "company": "Naver", "location": "서울시 강남구"},
            {"title": "고객관리 담당자", "company": "Kakao", "location": "제주시"},
            {"title": "AM (Account Manager)", "company": "SK텔레콤", "location": "서울시 강남구"},
            {"title": "고객성공팀", "company": "당근마켓", "location": "서울시 강남구"},
            {"title": "고객관리자", "company": "쿠팡", "location": "서울시 강남구"}
        ]
    },
    "기술/개발": {
        "백엔드 개발자": [
            {"title": "백엔드 개발자", "company": "쿠팡", "location": "서울시 강남구"},
            {"title": "Server Developer", "company": "Naver", "location": "서울시 강남구"},
            {"title": "백엔드 엔지니어", "company": "Kakao", "location": "서울시 강남구"},
            {"title": "Backend Software Engineer", "company": "당근마켓", "location": "서울시 강남구"},
            {"title": "Java 개발자", "company": "우아한형제들", "location": "서울시 강남구"}
        ],
        "프론트엔드 개발자": [
            {"title": "프론트엔드 개발자", "company": "당근마켓", "location": "서울시 강남구"},
            {"title": "Frontend Engineer", "company": "직방", "location": "서울시 중구"},
            {"title": "웹 개발자", "company": "숨고", "location": "서울시 강남구"},
            {"title": "React 개발자", "company": "토스", "location": "서울시 강남구"},
            {"title": "Frontend Developer", "company": "야놀자", "location": "서울시 강남구"}
        ],
        "클라우드 엔지니어": [
            {"title": "클라우드 엔지니어", "company": "Naver", "location": "서울시 강남구"},
            {"title": "Cloud Architect", "company": "Kakao", "location": "서울시 강남구"},
            {"title": "인프라 엔지니어", "company": "쿠팡", "location": "서울시 강남구"},
            {"title": "DevOps Engineer", "company": "당근마켓", "location": "서울시 강남구"},
            {"title": "클라우드 운영자", "company": "라이젠", "location": "서울시 강남구"}
        ]
    }
}

INTERVIEW_DATA: Dict[str, List[Dict]] = {
    "마케팅": [
        {
            "title": "마케팅 직무자의 하루 - 출근부터 퇴근까지",
            "link": "https://www.youtube.com/embed/W-8ydXqWEAo",
            "thumbnail": "https://i.ytimg.com/vi/W-8ydXqWEAo/maxresdefault.jpg"
        },
        {
            "title": "디지털 마케터의 일상 브이로그",
            "link": "https://www.youtube.com/embed/HGsGmXDIpSU",
            "thumbnail": "https://i.ytimg.com/vi/HGsGmXDIpSU/maxresdefault.jpg"
        },
        {
            "title": "마케팅 분석가 출근 일상",
            "link": "https://www.youtube.com/embed/kYbv0YPeNMg",
            "thumbnail": "https://i.ytimg.com/vi/kYbv0YPeNMg/maxresdefault.jpg"
        }
    ],
    "제조": [
        {
            "title": "제조업 생산관리자의 하루",
            "link": "https://www.youtube.com/embed/oBJKxOi0Noo",
            "thumbnail": "https://i.ytimg.com/vi/oBJKxOi0Noo/maxresdefault.jpg"
        },
        {
            "title": "공장 생산기술자 일상 브이로그",
            "link": "https://www.youtube.com/embed/Ys3h4FPhOkE",
            "thumbnail": "https://i.ytimg.com/vi/Ys3h4FPhOkE/maxresdefault.jpg"
        },
        {
            "title": "품질관리자의 출근 일상",
            "link": "https://www.youtube.com/embed/5JxGq5TJr80",
            "thumbnail": "https://i.ytimg.com/vi/5JxGq5TJr80/maxresdefault.jpg"
        }
    ],
    "행정": [
        {
            "title": "공공기관 행정가의 하루",
            "link": "https://www.youtube.com/embed/sRxAO1lYv9I",
            "thumbnail": "https://i.ytimg.com/vi/sRxAO1lYv9I/maxresdefault.jpg"
        },
        {
            "title": "기업 행정팀 일상 브이로그",
            "link": "https://www.youtube.com/embed/7t0vHoAb0eg",
            "thumbnail": "https://i.ytimg.com/vi/7t0vHoAb0eg/maxresdefault.jpg"
        },
        {
            "title": "인사담당자의 출근 일상",
            "link": "https://www.youtube.com/embed/W-8ydXqWEAo",
            "thumbnail": "https://i.ytimg.com/vi/W-8ydXqWEAo/maxresdefault.jpg"
        }
    ],
    "영업": [
        {
            "title": "B2B 영업사원의 하루",
            "link": "https://www.youtube.com/embed/HGsGmXDIpSU",
            "thumbnail": "https://i.ytimg.com/vi/HGsGmXDIpSU/maxresdefault.jpg"
        },
        {
            "title": "영업 담당자 출근 브이로그",
            "link": "https://www.youtube.com/embed/kYbv0YPeNMg",
            "thumbnail": "https://i.ytimg.com/vi/kYbv0YPeNMg/maxresdefault.jpg"
        },
        {
            "title": "Account Manager의 일상",
            "link": "https://www.youtube.com/embed/W-8ydXqWEAo",
            "thumbnail": "https://i.ytimg.com/vi/W-8ydXqWEAo/maxresdefault.jpg"
        }
    ],
    "기술/개발": [
        {
            "title": "백엔드 개발자의 하루",
            "link": "https://www.youtube.com/embed/oBJKxOi0Noo",
            "thumbnail": "https://i.ytimg.com/vi/oBJKxOi0Noo/maxresdefault.jpg"
        },
        {
            "title": "프론트엔드 개발자 출근 브이로그",
            "link": "https://www.youtube.com/embed/Ys3h4FPhOkE",
            "thumbnail": "https://i.ytimg.com/vi/Ys3h4FPhOkE/maxresdefault.jpg"
        },
        {
            "title": "클라우드 엔지니어의 일상",
            "link": "https://www.youtube.com/embed/5JxGq5TJr80",
            "thumbnail": "https://i.ytimg.com/vi/5JxGq5TJr80/maxresdefault.jpg"
        }
    ],
    "금융": [
        {
            "title": "투자 분석가의 하루",
            "link": "https://www.youtube.com/embed/sRxAO1lYv9I",
            "thumbnail": "https://i.ytimg.com/vi/sRxAO1lYv9I/maxresdefault.jpg"
        },
        {
            "title": "금융사 직원 출근 브이로그",
            "link": "https://www.youtube.com/embed/7t0vHoAb0eg",
            "thumbnail": "https://i.ytimg.com/vi/7t0vHoAb0eg/maxresdefault.jpg"
        },
        {
            "title": "금융 상담사의 일상",
            "link": "https://www.youtube.com/embed/HGsGmXDIpSU",
            "thumbnail": "https://i.ytimg.com/vi/HGsGmXDIpSU/maxresdefault.jpg"
        }
    ],
    "의료/헬스케어": [
        {
            "title": "간호사의 하루",
            "link": "https://www.youtube.com/embed/kYbv0YPeNMg",
            "thumbnail": "https://i.ytimg.com/vi/kYbv0YPeNMg/maxresdefault.jpg"
        },
        {
            "title": "의료 행정가 출근 브이로그",
            "link": "https://www.youtube.com/embed/W-8ydXqWEAo",
            "thumbnail": "https://i.ytimg.com/vi/W-8ydXqWEAo/maxresdefault.jpg"
        },
        {
            "title": "의료 기술 전문가의 일상",
            "link": "https://www.youtube.com/embed/oBJKxOi0Noo",
            "thumbnail": "https://i.ytimg.com/vi/oBJKxOi0Noo/maxresdefault.jpg"
        }
    ],
    "교육": [
        {
            "title": "교사의 하루",
            "link": "https://www.youtube.com/embed/Ys3h4FPhOkE",
            "thumbnail": "https://i.ytimg.com/vi/Ys3h4FPhOkE/maxresdefault.jpg"
        },
        {
            "title": "교육 기획자 출근 브이로그",
            "link": "https://www.youtube.com/embed/5JxGq5TJr80",
            "thumbnail": "https://i.ytimg.com/vi/5JxGq5TJr80/maxresdefault.jpg"
        },
        {
            "title": "에드테크 개발자의 일상",
            "link": "https://www.youtube.com/embed/sRxAO1lYv9I",
            "thumbnail": "https://i.ytimg.com/vi/sRxAO1lYv9I/maxresdefault.jpg"
        }
    ],
    "디자인": [
        {
            "title": "UI/UX 디자이너의 하루",
            "link": "https://www.youtube.com/embed/7t0vHoAb0eg",
            "thumbnail": "https://i.ytimg.com/vi/7t0vHoAb0eg/maxresdefault.jpg"
        },
        {
            "title": "그래픽 디자이너 출근 브이로그",
            "link": "https://www.youtube.com/embed/HGsGmXDIpSU",
            "thumbnail": "https://i.ytimg.com/vi/HGsGmXDIpSU/maxresdefault.jpg"
        },
        {
            "title": "브랜드 디자이너의 일상",
            "link": "https://www.youtube.com/embed/kYbv0YPeNMg",
            "thumbnail": "https://i.ytimg.com/vi/kYbv0YPeNMg/maxresdefault.jpg"
        }
    ],
    "법률": [
        {
            "title": "법무사의 하루",
            "link": "https://www.youtube.com/embed/W-8ydXqWEAo",
            "thumbnail": "https://i.ytimg.com/vi/W-8ydXqWEAo/maxresdefault.jpg"
        },
        {
            "title": "기업 법무팀 출근 브이로그",
            "link": "https://www.youtube.com/embed/oBJKxOi0Noo",
            "thumbnail": "https://i.ytimg.com/vi/oBJKxOi0Noo/maxresdefault.jpg"
        },
        {
            "title": "법률 전문가의 일상",
            "link": "https://www.youtube.com/embed/Ys3h4FPhOkE",
            "thumbnail": "https://i.ytimg.com/vi/Ys3h4FPhOkE/maxresdefault.jpg"
        }
    ]
}

# 직무별 세부 정보
JOB_DETAILS: Dict[str, Dict] = {
    "마케팅": {
        "Product Manager": {
            "short_desc": "상품 기획 및 시장 전략 수립",
            "detailed_desc": "Product Manager는 시장 조사, 경쟁 분석, 고객 피드백을 바탕으로 상품 전략을 수립하고 개발 팀과 협력하여 시장에 맞는 상품을 출시합니다. 상품의 생명주기 전반을 관리하며 매출 목표 달성을 위해 마케팅, 영업 팀과 긴밀히 협력합니다.\n\n**주요 업무:**\n• 시장 조사 및 경쟁사 분석\n• 상품 로드맵 수립 및 관리\n• 개발팀과 협력하여 상품 개발 주도\n• 가격 결정 및 출시 전략 수립\n• 마케팅 및 영업팀과 협력",
            "salary": "4,500~6,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=Product+Manager"
        },
        "Digital Marketing": {
            "short_desc": "온라인 광고 및 SNS 마케팅 전략 수립",
            "detailed_desc": "디지털 마케팅 전문가는 소셜 미디어, 검색 엔진 광고(SEM), 콘텐츠 마케팅 등 다양한 온라인 채널을 활용하여 브랜드 인지도를 높이고 고객을 확보합니다. 데이터 분석을 통해 캠페인 효과를 측정하고 지속적으로 최적화하는 역할을 합니다.\n\n**주요 업무:**\n• SNS 캠페인 기획 및 실행\n• Google Ads, Facebook Ads 등 광고 운영\n• 콘텐츠 마케팅 전략 수립\n• 캠페인 성과 분석 및 최적화\n• 고객 행동 분석 및 인사이트 도출",
            "salary": "3,500~5,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=Digital+Marketing"
        },
        "마케팅 분석가": {
            "short_desc": "데이터 기반 마케팅 효과 측정 및 분석",
            "detailed_desc": "마케팅 분석가는 고급 분석 도구와 통계 기법을 사용하여 마케팅 캠페인의 ROI를 측정하고, 고객 행동을 분석하며, 향후 마케팅 전략을 수립하기 위한 인사이트를 제공합니다. 데이터 해석 능력과 비즈니스 센스가 중요합니다.\n\n**주요 업무:**\n• 마케팅 캠프 성과 측정 및 분석\n• 고객 세분화 및 행동 분석\n• 대시보드 개발 및 리포팅\n• A/B 테스트 설계 및 분석\n• 데이터 기반 인사이트 제시",
            "salary": "4,000~6,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=마케팅+분석가"
        }
    },
    "제조": {
        "생산관리": {
            "short_desc": "공장 생산 계획 및 품질 관리",
            "detailed_desc": "생산관리자는 생산 계획 수립, 일정 관리, 원자재 조달, 작업 지시 등을 통해 효율적인 생산 프로세스를 운영합니다. 원가 절감, 납기 준수, 품질 유지 등 다양한 목표를 동시에 달성해야 하므로 높은 업무 조정 능력이 필요합니다.\n\n**주요 업무:**\n• 월간/주간 생산 계획 수립\n• 원자재 재고 관리\n• 생산 일정 조정 및 모니터링\n• 원가 분석 및 효율성 개선\n• 현장 감독 및 작업 지시",
            "salary": "3,500~5,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=생산관리"
        },
        "생산기술": {
            "short_desc": "공정 개선 및 기술 지원",
            "detailed_desc": "생산기술자는 생산 설비의 최적화, 공정 개선, 기술 문제 해결 등을 담당합니다. 제조 기술을 지속적으로 개선하고 신기술을 도입하여 생산성과 품질을 향상시킵니다. 엔지니어링 지식과 문제해결 능력이 중요합니다.\n\n**주요 업무:**\n• 생산 공정 개선 및 혁신\n• 설비 유지보수 및 관리\n• 신기술 도입 검토 및 추진\n• 공정 문제 분석 및 해결\n• 생산성 향상 프로젝트 관리",
            "salary": "4,000~6,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=생산기술"
        },
        "품질관리(QC)": {
            "short_desc": "제품 검사 및 품질 기준 유지",
            "detailed_desc": "품질관리자는 생산 과정의 각 단계에서 제품을 검사하고, 부정 제품을 발견하여 출고 전에 제거합니다. 품질 기준을 설정하고, 불량 원인을 분석하여 개선안을 제시하는 데 중요한 역할을 합니다.\n\n**주요 업무:**\n• 제품 검사 및 테스트\n• 품질 기준 설정 및 관리\n• 부정 원인 분석 (문제 분석)\n• 개선안 도출 및 추진\n• 공급처 품질 평가 및 관리",
            "salary": "3,200~5,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=QC"
        }
    },
    "행정": {
        "기업 행정": {
            "short_desc": "인사, 총무, 법무 등 행정 업무",
            "detailed_desc": "기업 행정 담당자는 인사 시스템 운영, 계약 관리, 법률 준수, 사무 환경 관리 등 기업의 모든 행정 업무를 담당합니다. 다양한 부서와 협력하며 기업의 효율적인 운영을 지원하는 중추적 역할을 수행합니다.\n\n**주요 업무:**\n• 급여, 인사기록 관리\n• 계약서 작성 및 관리\n• 법률 준수 및 컴플라이언스\n• 사무용품 구매 및 관리\n• 주주총회, 이사회 운영 지원",
            "salary": "3,000~5,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=행정"
        },
        "공공기관 행정": {
            "short_desc": "공무원 및 공공기관 행정 업무",
            "detailed_desc": "공공기관 행정가는 법령을 준수하면서 공공 서비스를 제공하는 업무를 담당합니다. 민원 처리, 정책 추진, 예산 관리 등 공익을 위한 행정 업무를 수행하며 공정성과 투명성이 특히 중요합니다.\n\n**주요 업무:**\n• 민원 접수 및 처리\n• 정책 안내 및 설명\n• 예산 편성 및 관리\n• 행정 서류 작성 및 관리\n• 관련 법령 준수 및 감시",
            "salary": "3,500~5,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=공무원"
        },
        "인사담당자": {
            "short_desc": "채용, 인사 관리 및 교육",
            "detailed_desc": "인사담당자는 채용 프로세스 운영, 직원 정보 관리, 급여 처리, 인사평가 시스템 운영, 직원 교육 프로그램 기획 등을 담당합니다. 직원과 회사의 상생을 도모하며 기업 문화 형성에 중요한 역할을 합니다.\n\n**주요 업무:**\n• 채용 공고 작성 및 채용 프로세스 운영\n• 직원 입사, 퇴사 관리\n• 급여, 복리후생 관리\n• 인사평가 및 승진 관리\n• 직원 교육 및 개발 프로그램 기획",
            "salary": "3,500~5,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=인사담당자"
        }
    },
    "영업": {
        "B2B 영업": {
            "short_desc": "기업 대상 영업 및 계약 관리",
            "detailed_desc": "B2B 영업사원은 기업 고객을 대상으로 제품이나 서비스를 판매합니다. 장기적인 관계 형성, 복잡한 계약 협상, 고객 니즈에 맞는 솔루션 제시 등의 업무를 수행하며, 높은 금액의 거래를 담당하므로 협상 능력과 신뢰 구축이 중요합니다.\n\n**주요 업무:**\n• 신규 고객 발굴 및 영업 활동\n• 기업 고객 니즈 파악 및 솔루션 제시\n• 계약 협상 및 거래 체결\n• 계약서 작성 및 법무 검토\n• 고객 방문 및 관계 관리",
            "salary": "3,500~7,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=B2B+영업"
        },
        "B2C 영업": {
            "short_desc": "개인 고객 대상 영업",
            "detailed_desc": "B2C 영업사원은 일반 소비자를 대상으로 제품이나 서비스를 판매합니다. 고객 심리 이해, 상품 설명, 이의 제기 처리 등 다양한 상황에 대응하는 능력이 필요하며, 직접 대면 또는 온라인으로 고객을 만납니다.\n\n**주요 업무:**\n• 상품/서비스 설명 및 상담\n• 고객 질문 답변 및 이의 대응\n• 판매 계약 체결\n• 고객 불만 처리\n• 재구매 고객 관리",
            "salary": "3,000~6,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=영업"
        },
        "Account Manager": {
            "short_desc": "기존 고객 관계 관리 및 성장 전략",
            "detailed_desc": "Account Manager는 기존 고객과의 장기적인 관계를 유지하고, 고객 만족도를 높이며, 추가 제품 판매 기회를 발굴합니다. 고객의 비즈니스를 이해하고 파트너처럼 협력하여 상호 성장을 도모하는 전략적 영업 역할입니다.\n\n**주요 업무:**\n• 기존 고객 관계 유지 및 강화\n• 고객 만족도 조사 및 피드백 수집\n• 추가 판매 기회 발굴 및 제시\n• 고객 비즈니스 이해 및 지원\n• 계약 갱신 및 성장 전략 수립",
            "salary": "4,000~6,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=Account+Manager"
        }
    },
    "기술/개발": {
        "백엔드 개발자": {
            "short_desc": "서버 및 데이터베이스 개발",
            "detailed_desc": "백엔드 개발자는 서버 시스템, 데이터베이스, API 등 애플리케이션의 핵심 로직을 개발합니다. 사용자가 보지 못하는 뒤쪽에서 시스템이 안정적으로 작동하도록 설계하고 구현하며, 확장성과 보안이 중요합니다.\n\n**주요 업무:**\n• 서버 개발 및 유지보수\n• 데이터베이스 설계 및 최적화\n• API 개발 및 통합\n• 시스템 성능 개선\n• 보안 취약점 분석 및 개선",
            "salary": "4,500~8,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=백엔드"
        },
        "프론트엔드 개발자": {
            "short_desc": "웹/앱 UI/UX 개발",
            "detailed_desc": "프론트엔드 개발자는 사용자가 직접 보고 상호작용하는 웹/앱 화면을 개발합니다. HTML, CSS, JavaScript를 활용하여 아름답고 사용하기 쉬운 인터페이스를 만들며, UX/UI 디자인과 개발을 연결하는 중요한 역할입니다.\n\n**주요 업무:**\n• 웹/앱 화면 개발\n• UI/UX 구현\n• 반응형 디자인 적용\n• 성능 최적화\n• 브라우저 호환성 테스트",
            "salary": "4,500~8,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=프론트엔드"
        },
        "클라우드 엔지니어": {
            "short_desc": "클라우드 인프라 구축 및 관리",
            "detailed_desc": "클라우드 엔지니어는 AWS, Azure, GCP 등 클라우드 플랫폼을 이용하여 IT 인프라를 구축하고 관리합니다. 확장성, 보안, 비용 효율성을 모두 고려한 시스템 설계와 운영이 핵심입니다.\n\n**주요 업무:**\n• 클라우드 인프라 설계 및 구축\n• 서버 및 네트워크 관리\n• 데이터 백업 및 재해 복구\n• 보안 및 접근 제어 관리\n• 비용 최적화 및 모니터링",
            "salary": "5,000~9,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=클라우드"
        }
    },
    "금융": {
        "투자 분석가": {
            "short_desc": "기업/주식 분석 및 투자 권고",
            "detailed_desc": "투자 분석가는 기업 재무제표, 산업 동향, 거시경제 지표 등을 분석하여 투자 의견을 제시합니다. 깊은 재무 분석 능력과 시장 이해를 바탕으로 포트폴리오 관리와 투자 수익 창출을 목표로 합니다.\n\n**주요 업무:**\n• 기업 재무 분석\n• 산업 및 시장 분석\n• 투자 보고서 작성\n• 투자 포트폴리오 관리\n• 투자자 상담 및 설명",
            "salary": "4,500~8,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=투자분석가"
        },
        "리스크 관리": {
            "short_desc": "금융 리스크 측정 및 관리",
            "detailed_desc": "리스크 관리자는 금융 기관이 직면한 다양한 리스크(신용 리스크, 시장 리스크, 유동성 리스크 등)를 측정하고 통제합니다. 규제 요건을 만족하면서 리스크와 수익의 균형을 맞추는 중요한 역할입니다.\n\n**주요 업무:**\n• 금융 리스크 측정 및 모니터링\n• 리스크 모델 개발 및 운영\n• 규제 준수 및 보고\n• 리스크 노출 제한 설정\n• 리스크 완화 전략 수립",
            "salary": "4,500~7,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=리스크+관리"
        },
        "금융 상담사": {
            "short_desc": "고객 자산 관리 및 투자 상담",
            "detailed_desc": "금융 상담사는 개인 고객의 재무 상황을 파악하고 그에 맞는 투자 상품을 추천합니다. 신뢰 관계 구축, 고객 니즈 이해, 금융 상품 지식이 중요하며 고객 자산 증식을 도모합니다.\n\n**주요 업무:**\n• 고객 재무 상황 파악\n• 투자 상품 설명 및 추천\n• 포트폴리오 관리 및 리밸런싱\n• 고객 상담 및 교육\n• 규제 준수 및 서류 관리",
            "salary": "3,500~6,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=금융+상담사"
        }
    },
    "의료/헬스케어": {
        "간호사": {
            "short_desc": "환자 진료 보조 및 건강 관리",
            "detailed_desc": "간호사는 환자의 건강 상태를 관찰하고 의사의 지시에 따라 의료 처치를 수행합니다. 환자의 신체적, 정신적 안위를 위해 노력하며 높은 책임감과 공감 능력이 필요합니다.\n\n**주요 업무:**\n• 환자 활력징후 측정 및 기록\n• 의료 처치 수행\n• 약물 투여 및 관리\n• 환자 상담 및 교육\n• 의료 기록 관리",
            "salary": "3,500~4,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=간호사"
        },
        "의료 행정": {
            "short_desc": "병원 행정 및 의무기록 관리",
            "detailed_desc": "의료 행정가는 병원 운영의 행정적 측면을 담당합니다. 환자 접수, 의무기록 관리, 보험 청구, 예약 관리 등 의료 기관의 효율적 운영을 지원합니다.\n\n**주요 업무:**\n• 환자 접수 및 등록\n• 의무기록 작성 및 관리\n• 건강보험 청구\n• 진료 예약 관리\n• 환자 상담 및 민원 처리",
            "salary": "3,000~4,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=의료+행정"
        },
        "의료 기술 전문가": {
            "short_desc": "의료 장비 및 시스템 운영",
            "detailed_desc": "의료 기술 전문가는 CT, MRI, 초음파 등 의료 장비를 운영하고 환자 검사를 수행합니다. 정확한 검사 수행과 장비 관리가 중요하며 환자 안전이 최우선입니다.\n\n**주요 업무:**\n• 의료 장비 운영\n• 환자 검사 수행\n• 검사 영상/데이터 기록\n• 장비 일일 점검 및 유지보수\n• 의료 안전 준수",
            "salary": "3,500~5,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=의료+기술"
        }
    },
    "교육": {
        "교사": {
            "short_desc": "학생 교육 및 학습 관리",
            "detailed_desc": "교사는 학생들에게 지식을 전달하고 학습을 지도합니다. 다양한 학습 방법을 활용하여 학생의 이해를 돕고, 인성 발달과 진로 지도도 중요한 역할입니다.\n\n**주요 업무:**\n• 교과 수업 진행\n• 학생 평가 및 성적 관리\n• 학습 자료 개발\n• 진로 상담 및 지도\n• 학부모 면담 및 소통",
            "salary": "3,500~5,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=교사"
        },
        "교육 기획자": {
            "short_desc": "교육 프로그램 개발 및 운영",
            "detailed_desc": "교육 기획자는 효과적인 교육 프로그램을 개발하고 운영합니다. 학습자의 니즈를 파악하고 그에 맞는 교육 목표와 내용을 설계하며 지속적으로 개선합니다.\n\n**주요 업무:**\n• 교육 프로그램 기획 및 설계\n• 학습 목표 설정 및 평가 기준 개발\n• 교육 콘텐츠 개발\n• 교사 교육 및 지원\n• 프로그램 효과성 평가",
            "salary": "3,500~5,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=교육+기획"
        },
        "에드테크 개발자": {
            "short_desc": "온라인 교육 플랫폼 개발",
            "detailed_desc": "에드테크 개발자는 온라인 교육을 지원하는 기술 플랫폼을 개발합니다. 학습 효과를 극대화하는 사용자 경험과 강력한 기술 시스템을 함께 구현합니다.\n\n**주요 업무:**\n• 온라인 학습 플랫폼 개발\n• 교육 콘텐츠 관리 시스템 구축\n• 학생 진도 추적 시스템 개발\n• 모바일 교육 앱 개발\n• AI를 활용한 맞춤형 학습 기능 개발",
            "salary": "4,500~8,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=에드테크"
        }
    },
    "디자인": {
        "UI/UX 디자이너": {
            "short_desc": "사용자 중심 인터페이스 설계",
            "detailed_desc": "UI/UX 디자이너는 사용자 연구를 바탕으로 직관적이고 사용하기 쉬운 인터페이스를 설계합니다. 사용자 경험을 깊이 있게 이해하고 그것을 시각적으로 구현하는 역할입니다.\n\n**주요 업무:**\n• 사용자 조사 및 분석\n• 와이어프레임 및 프로토타입 제작\n• UI 화면 디자인\n• 사용성 테스트 및 개선\n• 디자인 시스템 개발",
            "salary": "3,500~6,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=UI+UX"
        },
        "그래픽 디자이너": {
            "short_desc": "광고 및 마케팅 자료 디자인",
            "detailed_desc": "그래픽 디자이너는 시각적으로 매력적인 광고, 포스터, 패키지 등을 디자인합니다. 브랜드 메시지를 효과적으로 전달하는 시각 디자인을 창출합니다.\n\n**주요 업무:**\n• 광고 및 마케팅 자료 디자인\n• 브로셔 및 팜플렛 제작\n• 패키지 디자인\n• 인쇄물 디자인\n• 디자인 트렌드 연구",
            "salary": "3,000~5,500만원",
            "job_url": "https://www.wanted.co.kr/search?query=그래픽+디자인"
        },
        "브랜드 디자이너": {
            "short_desc": "브랜드 아이덴티티 개발 및 관리",
            "detailed_desc": "브랜드 디자이너는 기업의 브랜드 가치를 시각적으로 표현하는 로고, 색상, 타이포그래피 등을 개발합니다. 일관된 브랜드 이미지를 유지하도록 관리하는 역할입니다.\n\n**주요 업무:**\n• 로고 및 심볼 디자인\n• 브랜드 컬러 및 타이포그래피 개발\n• 브랜드 가이드라인 작성\n• 브랜드 애셋 관리\n• 브랜드 리뉴얼 프로젝트 진행",
            "salary": "3,500~6,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=브랜드+디자인"
        }
    },
    "법률": {
        "법무사": {
            "short_desc": "법무 자문 및 소송 관리",
            "detailed_desc": "법무사는 의뢰인을 대리하여 법적 자문을 제공하고 소송을 진행합니다. 법률 지식을 바탕으로 의뢰인의 권리를 보호하고 분쟁을 해결하는 전문가입니다.\n\n**주요 업무:**\n• 법률 자문 및 상담\n• 계약서 검토 및 작성\n• 소송 대리\n• 합의 중재\n• 법적 문서 작성",
            "salary": "5,000~9,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=법무사"
        },
        "기업 법무": {
            "short_desc": "기업 법률 자문 및 계약 관리",
            "detailed_desc": "기업 법무 담당자는 기업의 모든 법률 사항을 관리합니다. 계약 체결, 규제 준수, 분쟁 해결 등을 통해 기업의 법적 리스크를 최소화합니다.\n\n**주요 업무:**\n• 기업 계약 검토 및 관리\n• 규제 준수 확인\n• 노사 분쟁 해결\n• 지적재산권 관리\n• 법적 리스크 분석 및 대응",
            "salary": "4,500~8,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=법무"
        },
        "법률 전문가": {
            "short_desc": "법률 자문 및 분석",
            "detailed_desc": "법률 전문가는 특정 분야(세무, 노동, 국제법 등)의 깊이 있는 법률 전문 지식을 제공합니다. 개인과 기업의 복잡한 법적 문제를 해결하는 역할입니다.\n\n**주요 업무:**\n• 전문 분야 법률 자문\n• 법률 분석 및 의견서 작성\n• 규제 변화 모니터링\n• 법률 교육 및 강의\n• 정책 자문 및 제안",
            "salary": "5,000~10,000만원",
            "job_url": "https://www.wanted.co.kr/search?query=법률+전문가"
        }
    }
}

# 앱 헤더 섹션
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem 2rem; border-radius: 20px; margin-bottom: 2rem; text-align: center;">
    <h1 style="color: white; font-size: 2.2rem; margin: 0; font-weight: 800;">🎬 멘토 생성기</h1>
</div>
""", unsafe_allow_html=True)

# 멘토 이미지 섹션
st.markdown("""
<div style="display: flex; justify-content: center; gap: 1.5rem; margin-bottom: 2rem; flex-wrap: wrap;">
    <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&h=150&fit=crop" style="border-radius: 50%; width: 90px; height: 90px; border: 3px solid #667eea; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);">
    <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop" style="border-radius: 50%; width: 90px; height: 90px; border: 3px solid #667eea; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);">
    <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=150&h=150&fit=crop" style="border-radius: 50%; width: 90px; height: 90px; border: 3px solid #667eea; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);">
    <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&h=150&fit=crop" style="border-radius: 50%; width: 90px; height: 90px; border: 3px solid #667eea; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);">
</div>
""", unsafe_allow_html=True)

# 부제목 헤더 섹션
st.markdown("""
<div style="background: linear-gradient(135deg, #f0f4ff 0%, #f5f0ff 100%); padding: 2rem; border-radius: 15px; margin-bottom: 2rem; border-left: 5px solid #667eea; text-align: center;">
    <h2 style="color: #667eea; font-size: 1.5rem; margin: 0 0 1rem 0; font-weight: 700;">🎯 멘토 생성기에 오신 것을 환영합니다</h2>
    <p style="color: #555; font-size: 1rem; margin: 0; line-height: 1.6;">
        현직자의 실제 업무 경험을 통해 당신의 꿈의 직업을 발견하세요.<br>
        마케팅, 제조, 행정, 영업, 기술/개발, 금융, 의료, 교육, 디자인, 법률 등<br>
        다양한 직무 분야의 현직자들이 하루하루 어떻게 일하는지 살펴보고,<br>
        실제 채용공고까지 확인할 수 있습니다. 당신의 미래 커리어를 함께 준비해보세요!
    </p>
</div>
""", unsafe_allow_html=True)

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

# 추천 결과 표시
if recommend_button or "show_results" not in st.session_state:
    st.session_state.selected_field = selected_field
    st.session_state.selected_job = selected_job
    st.session_state.show_results = True

if st.session_state.get("show_results", False):
    # 선택한 분야 표시 (작은 세련된 바)
    current_field = st.session_state.get('selected_field', selected_field)
    current_job = st.session_state.get('selected_job', selected_job)
    
    st.markdown(f"""
    <div style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); padding: 0.4rem 1rem; border-radius: 8px; margin-bottom: 2rem; text-align: center;">
        <span style="color: white; font-weight: 600; font-size: 0.85rem;">📌 {current_field} &gt; 💼 {current_job}</span>
    </div>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="result-section">', unsafe_allow_html=True)
        
        # 제목 스타일 변경
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f0f4ff 0%, #f5f0ff 100%); padding: 0.8rem; border-radius: 12px; margin-bottom: 1.5rem; border-left: 5px solid #667eea;">
            <h3 style="margin: 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">🌟 {current_field} - {current_job} 멘토</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # 직무 정보
        job_info = JOB_DETAILS[current_field][current_job]
        
        # 직무 설명 섹션
        st.markdown(f'<div style="background: linear-gradient(135deg, #f0f4ff 0%, #f5f0ff 100%); padding: 1rem; border-radius: 12px; margin-bottom: 0.8rem; border-left: 5px solid #667eea;">', unsafe_allow_html=True)
        st.markdown(f"**💡 직무 설명**")
        st.markdown(f'<p class="small-text">{job_info["detailed_desc"]}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown(f'<div style="background: linear-gradient(135deg, #f0f4ff 0%, #f5f0ff 100%); padding: 1rem; border-radius: 12px; margin-bottom: 0.8rem; border-left: 5px solid #667eea;">', unsafe_allow_html=True)
        st.markdown(f"**💰 예상 연봉**")
        st.markdown(f'<p class="small-text">{job_info["salary"]}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 채용공고 링크 섹션
        st.markdown(f"**🔗 실제 채용공고 (3~5개 예시)**")
        postings = JOB_POSTINGS.get(current_field, {}).get(current_job, [])
        
        for posting in postings[:5]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #fff0f5 0%, #ffe4f0 100%); padding: 1rem; border-radius: 10px; margin-bottom: 0.8rem; border-left: 4px solid #e85b8a;">
                <strong>{posting['title']}</strong><br>
                <span style="font-size: 0.9rem; color: #555;">📍 {posting['company']} | {posting['location']}</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown(f"<a href='{job_info['job_url']}' target='_blank' style='display: inline-block; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 0.7rem 1.5rem; border-radius: 8px; text-decoration: none; margin-top: 1rem; font-weight: 600;'>원티드에서 더 많은 채용공고 보기 →</a>", unsafe_allow_html=True)
        
        st.markdown("### 📺 현직자의 하루")
        
        videos = INTERVIEW_DATA[current_field]
        
        # 3개씩 한 줄에 표시
        for i in range(0, len(videos), 3):
            cols = st.columns(3)
            for j, col in enumerate(cols):
                if i + j < len(videos):
                    video = videos[i + j]
                    with col:
                        st.markdown(f'<div class="video-card">', unsafe_allow_html=True)
                        st.image(video['thumbnail'], use_column_width=True)
                        st.markdown(f"**{i+j+1}. {video['title']}**")
                        st.markdown(f"[🎥 YouTube에서 보기]({video['link'].replace('embed/', 'watch?v=')})")
                        st.markdown(f"*3~5분 분량*")
        
        st.markdown('</div>', unsafe_allow_html=True)
