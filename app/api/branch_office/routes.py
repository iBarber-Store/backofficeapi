from flask import request
from app.api.branch_office import branch_office_bp
from app.model.common.base_response import BaseResponse
from app.model.database.branch_office import BranchOffice
from app.config.database import db_session
from sqlalchemy import exc

@branch_office_bp.route("/branchOffice", methods=["GET", "POST"])
@branch_office_bp.route("/branchOffice/<int:branchOfficeId>", methods=["GET", "PUT", "DELETE"])
def branchOfficeAdmin(branchOfficeId=None):
    if request.method == "POST":
        try:
            jsonBody = request.get_json()
            b = BranchOffice.from_dict(jsonBody)
            del b.id
            db_session.add(b)
            db_session.commit()
            return BaseResponse(
                code=0,
                msg="Branch office created successfuly",
                data=b.to_dict()
            ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Branch office couldn't be saved"
            ).to_dict()
    
    elif request.method == "GET":
        try:
            if branchOfficeId is None:
                branches = BranchOffice.query.all()
                branchesArr = []
                for b in branches:
                    branchesArr.append(b.to_dict())
                return BaseResponse(
                        code=0,
                        msg="Branch offices loaded successfuly",
                        data=branchesArr
                    ).to_dict()
            else:
                resultSet = db_session.query(BranchOffice).get(branchOfficeId)
                if(resultSet is not None):
                    branch = BranchOffice.from_dict(resultSet.__dict__)
                    branch.id = branchOfficeId
                    return BaseResponse(
                            code=0,
                            msg="Branch office loaded successfuly",
                            data=branch.to_dict()
                        ).to_dict()
                else:
                    return BaseResponse(
                            code=1,
                            msg="Branch office doesn't exists"
                        ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="An error ocurred"
            ).to_dict()
            
    elif request.method == "PUT":
        try:
            resultSet = db_session.query(BranchOffice).get(branchOfficeId)
            if(resultSet is not None):
                jsonBody = request.get_json()
                branchVal = BranchOffice.from_dict(jsonBody)
                branch = db_session.query(BranchOffice).filter(BranchOffice.id == branchOfficeId).one()
                branch.another_name = branchVal.another_name
                branch.description = branchVal.description
                branch.logo = branchVal.logo
                branch.branch = branchVal.branch
                db_session.commit()
                return BaseResponse(
                        code=0,
                        msg="Branch office updated successfuly",
                        data=branch.to_dict()
                    ).to_dict()
            else:
                return BaseResponse(
                        code=1,
                        msg="Branch office doesn't exists"
                    ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Branch office couldn't be updated"
                ).to_dict()
        
    elif request.method == "DELETE":
        try:
            db_session.query(BranchOffice).filter(BranchOffice.id == branchOfficeId).delete()
            db_session.commit()
            return BaseResponse(
                code=0,
                msg="Branch office deleted succesfully"
            ).to_dict()
        except exc.IntegrityError:
            return BaseResponse(
                code=1,
                msg="Branch office has more related data, delete those data first"
            ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Branch office couldn't be deleted"
            ).to_dict()
