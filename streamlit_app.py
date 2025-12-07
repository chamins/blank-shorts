import streamlit as st
from typing import Dict, List

# 페이지 설정
st.set_page_config(
    page_title="짧은 영상 추천 리스트 생성기",
    page_icon="🎬",
    layout="wide"
)

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

# 앱 제목
st.title("🎬 짧은 영상 추천 리스트 생성기")
st.markdown("현직자의 실무 인터뷰 영상으로 직업을 알아보세요!")
st.divider()

# UI 레이아웃
col1, col2 = st.columns([3, 1])

with col1:
    selected_field = st.selectbox(
        "관심 분야를 선택하세요",
        options=list(INTERVIEW_DATA.keys()),
        index=0
    )

with col2:
    st.write("")  # 높이 맞추기
    recommend_button = st.button("📺 추천 영상 보기", use_container_width=True)

st.divider()

# 추천 결과 표시
if recommend_button or "selected_field" not in st.session_state:
    st.session_state.selected_field = selected_field
    st.session_state.show_results = True

if st.session_state.get("show_results", False):
    st.subheader(f"✨ '{st.session_state.get('selected_field', selected_field)}' 분야 추천 영상")
    
    videos = INTERVIEW_DATA[st.session_state.get('selected_field', selected_field)]
    
    # 영상 표시
    for idx, video in enumerate(videos, 1):
        st.markdown(f"### 📌 {idx}. {video['title']}")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(video['thumbnail'], use_column_width=True)
        
        with col2:
            st.markdown(f"**영상 링크**: [{video['title']}]({video['link']})")
            st.markdown(f"[YouTube에서 보기 🔗](https://www.youtube.com/watch?v={video['link'].split('embed/')[-1]})")
        
        st.divider()
