from dataclasses import dataclass
from app.domain.assessments.assessment import Assessment
from app.domain.sessions.session import SessaoDASS21
@dataclass
class SessionService:


    def create_session(self) -> SessaoDASS21:
        session = SessaoDASS21()
        assessment = Assessment()

        session.start()
        session.assessment = assessment
    
        return session

   
