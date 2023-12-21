from flask import request
from app.api.branch_office_detail import branch_office_detail_bp
from app.model.common.base_response import BaseResponse
from app.model.database.branch_office_detail import BranchOfficeDetail
from app.config.database import db_session
from sqlalchemy import exc

@branch_office_detail_bp.route("/branchOffice/detail", methods=["GET", "POST"])
@branch_office_detail_bp.route("/branchOffice/detail/<int:branchOfficeDetailId>", methods=["GET", "PUT", "DELETE"])
def branchAdmin(branchOfficeDetailId=None):
    if request.method == "POST":
        try:
            jsonBody = request.get_json()
            b = BranchOfficeDetail.from_dict(jsonBody)
            del b.id
            db_session.add(b)
            db_session.commit()
            return BaseResponse(
                code=0,
                msg="Branch office detail created successfuly",
                data=b.to_dict()
            ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Branch office detail couldn't be saved"
            ).to_dict()
    
    elif request.method == "GET":
        try:
            if branchOfficeDetailId is None:
                branches = BranchOfficeDetail.query.all()
                branchesArr = []
                for b in branches:
                    branchesArr.append(b.to_dict())
                return BaseResponse(
                        code=0,
                        msg="Branches office details loaded successfuly",
                        data=branchesArr
                    ).to_dict()
            else:
                resultSet = db_session.query(BranchOfficeDetail).get(branchOfficeDetailId)
                if(resultSet is not None):
                    branch = BranchOfficeDetail.from_dict(resultSet.__dict__)
                    branch.id = branchOfficeDetailId
                    return BaseResponse(
                            code=0,
                            msg="Branch office detail loaded successfuly",
                            data=branch.to_dict()
                        ).to_dict()
                else:
                    return BaseResponse(
                            code=1,
                            msg="Branch office detail doesn't exists"
                        ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="An error ocurred"
            ).to_dict()
            
    elif request.method == "PUT":
        try:
            resultSet = db_session.query(BranchOfficeDetail).get(branchOfficeDetailId)
            if(resultSet is not None):
                jsonBody = request.get_json()
                branchVal = BranchOfficeDetail.from_dict(jsonBody)
                branch = db_session.query(BranchOfficeDetail).filter(BranchOfficeDetail.id == branchOfficeDetailId).one()
                branch.hair_cut_duration = branchVal.hair_cut_duration
                branch.qualifying = branchVal.qualifying
                branch.ratings = branchVal.ratings
                branch.branch_office = branchVal.branch_office
                db_session.commit()
                return BaseResponse(
                        code=0,
                        msg="Branch office detail updated successfuly",
                        data=branch.to_dict()
                    ).to_dict()
            else:
                return BaseResponse(
                        code=1,
                        msg="Branch office detail doesn't exists"
                    ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Branch office detail couldn't be updated"
                ).to_dict()
        
    elif request.method == "DELETE":
        try:
            db_session.query(BranchOfficeDetail).filter(BranchOfficeDetail.id == branchOfficeDetailId).delete()
            db_session.commit()
            return BaseResponse(
                code=0,
                msg="Branch office detail deleted succesfully"
            ).to_dict()
        except exc.IntegrityError:
            return BaseResponse(
                code=1,
                msg="Branch office detail has more related data, delete those data first"
            ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Branch office detail couldn't be deleted"
            ).to_dict()
