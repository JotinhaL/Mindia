from uuid import UUID

from sqlalchemy.orm import Session

from app.models.assessment import AssessmentModel


class AssessmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, session_id: UUID | None = None) -> AssessmentModel:
        assessment = AssessmentModel(session_id=session_id)
        self.db.add(assessment)
        self.db.commit()
        self.db.refresh(assessment)
        return assessment

    def get_by_id(self, assessment_id: UUID) -> AssessmentModel | None:
        return self.db.query(AssessmentModel).filter(AssessmentModel.id == assessment_id).first()

    def get_by_session_id(self, session_id: UUID) -> AssessmentModel | None:
        return self.db.query(AssessmentModel).filter(AssessmentModel.session_id == session_id).first()

    def save(self, assessment: AssessmentModel) -> AssessmentModel:
        self.db.add(assessment)
        self.db.commit()
        self.db.refresh(assessment)
        return assessment

    def update(self, assessment: AssessmentModel, **fields) -> AssessmentModel:
        for attr, value in fields.items():
            if hasattr(assessment, attr):
                setattr(assessment, attr, value)
        self.db.commit()
        self.db.refresh(assessment)
        return assessment

    def delete(self, assessment: AssessmentModel) -> None:
        self.db.delete(assessment)
        self.db.commit()
