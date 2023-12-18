from flask import request
from app.branch import branch_bp
from app.model.common.base_response import BaseResponse
from app.model.database.branch import Branch
from app.config.database import db_session
from sqlalchemy import exc

@branch_bp.route("/branch", methods=["GET", "POST"])
@branch_bp.route("/branch/<int:branchId>", methods=["GET", "PUT", "DELETE"])
def branchAdmin(branchId=None):
    if request.method == "POST":
        try:
            jsonBody = request.get_json()
            b = Branch.from_dict(jsonBody)
            del b.id
            db_session.add(b)
            db_session.commit()
            return BaseResponse(
                code=0,
                msg="Branch created successfuly",
                data=b.to_dict()
            ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Branchd couldn't be saved"
            ).to_dict()
    
    elif request.method == "GET":
        try:
            if branchId is None:
                branches = Branch.query.all()
                branchesArr = []
                for b in branches:
                    branchesArr.append(b.to_dict())
                return BaseResponse(
                        code=0,
                        msg="Branches loaded successfuly",
                        data=branchesArr
                    ).to_dict()
            else:
                resultSet = db_session.query(Branch).get(branchId)
                if(resultSet is not None):
                    branch = Branch.from_dict(resultSet.__dict__)
                    branch.id = branchId
                    return BaseResponse(
                            code=0,
                            msg="Branch loaded successfuly",
                            data=branch.to_dict()
                        ).to_dict()
                else:
                    return BaseResponse(
                            code=1,
                            msg="Branch doesn't exists"
                        ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="An error ocurred"
            ).to_dict()
            
    elif request.method == "PUT":
        try:
            resultSet = db_session.query(Branch).get(branchId)
            if(resultSet is not None):
                jsonBody = request.get_json()
                branchVal = Branch.from_dict(jsonBody)
                branch = db_session.query(Branch).filter(Branch.id == branchId).one()
                branch.name = branchVal.name
                branch.alternative_name = branchVal.alternative_name
                branch.logo = branchVal.logo
                branch.enable = branchVal.enable
                branch.user_access = branchVal.user_access
                db_session.commit()
                return BaseResponse(
                        code=0,
                        msg="Branch updated successfuly",
                        data=branch.to_dict()
                    ).to_dict()
            else:
                return BaseResponse(
                        code=1,
                        msg="Branch doesn't exists"
                    ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Branch couldn't be updated"
                ).to_dict()
        
    elif request.method == "DELETE":
        try:
            db_session.query(Branch).filter(Branch.id == branchId).delete()
            db_session.commit()
            return BaseResponse(
                code=0,
                msg="Branch deleted succesfully"
            ).to_dict()
        except exc.IntegrityError:
            return BaseResponse(
                code=1,
                msg="Branch has more related data, delete those data first"
            ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Branch couldn't be deleted"
            ).to_dict()
