from flask import request
from app.api.photo_branch_office import photo_branch_office_bp
from app.model.common.base_response import BaseResponse
from app.model.database.photo_branch_office import PhotoBranchOffice
from app.config.database import db_session
from sqlalchemy import exc

@photo_branch_office_bp.route("/photoBranchOffice", methods=["GET", "POST"])
@photo_branch_office_bp.route("/photoBranchOffice/<int:photoBranchOfficeId>", methods=["GET", "PUT", "DELETE"])
def photoBranchOfficeAdmin(photoBranchOfficeId=None):
    if request.method == "POST":
        try:
            jsonBody = request.get_json()
            b = PhotoBranchOffice.from_dict(jsonBody)
            del b.id
            db_session.add(b)
            db_session.commit()
            return BaseResponse(
                code=0,
                msg="Photo branch office created successfuly",
                data=b.to_dict()
            ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Photo branch office couldn't be saved"
            ).to_dict()
    
    elif request.method == "GET":
        try:
            if photoBranchOfficeId is None:
                photos = PhotoBranchOffice.query.all()
                photosArr = []
                for p in photos:
                    photosArr.append(p.to_dict())
                return BaseResponse(
                        code=0,
                        msg="Photo branch offices loaded successfuly",
                        data=photosArr
                    ).to_dict()
            else:
                resultSet = db_session.query(PhotoBranchOffice).get(photoBranchOfficeId)
                if(resultSet is not None):
                    photo = PhotoBranchOffice.from_dict(resultSet.__dict__)
                    photo.id = photoBranchOfficeId
                    return BaseResponse(
                            code=0,
                            msg="Photo branch office loaded successfuly",
                            data=photo.to_dict()
                        ).to_dict()
                else:
                    return BaseResponse(
                            code=1,
                            msg="Photo branch office doesn't exists"
                        ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="An error ocurred"
            ).to_dict()
            
    elif request.method == "PUT":
        try:
            resultSet = db_session.query(PhotoBranchOffice).get(photoBranchOfficeId)
            if(resultSet is not None):
                jsonBody = request.get_json()
                photoVal = PhotoBranchOffice.from_dict(jsonBody)
                photo = db_session.query(PhotoBranchOffice).filter(PhotoBranchOffice.id == photoBranchOfficeId).one()
                photo.branch_office = photoVal.branch_office
                photo.file_path = photoVal.file_path
                photo.display_order = photoVal.display_order
                db_session.commit()
                return BaseResponse(
                        code=0,
                        msg="Photo branch office updated successfuly",
                        data=photo.to_dict()
                    ).to_dict()
            else:
                return BaseResponse(
                        code=1,
                        msg="Photo branch office doesn't exists"
                    ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Photo branch office couldn't be updated"
                ).to_dict()
        
    elif request.method == "DELETE":
        try:
            db_session.query(PhotoBranchOffice).filter(PhotoBranchOffice.id == photoBranchOfficeId).delete()
            db_session.commit()
            return BaseResponse(
                code=0,
                msg="Photo branch office deleted succesfully"
            ).to_dict()
        except exc.IntegrityError:
            return BaseResponse(
                code=1,
                msg="Photo branch office has more related data, delete those data first"
            ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Photo branch office couldn't be deleted"
            ).to_dict()
