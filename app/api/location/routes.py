from flask import request
from app.api.location import location_bp
from app.model.common.base_response import BaseResponse
from app.model.database.location import Location
from app.config.database import db_session
from sqlalchemy import exc

@location_bp.route("/location", methods=["GET", "POST"])
@location_bp.route("/location/<int:locationId>", methods=["GET", "PUT", "DELETE"])
def locationAdm(locationId=None):
    if request.method == "POST":
        try:
            jsonBody = request.get_json()
            b = Location.from_dict(jsonBody)
            del b.id
            db_session.add(b)
            db_session.commit()
            return BaseResponse(
                code=0,
                msg="Location created successfuly",
                data=b.to_dict()
            ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Location couldn't be saved"
            ).to_dict()
    
    elif request.method == "GET":
        try:
            if locationId is None:
                locations = Location.query.all()
                locationsArr = []
                for l in locations:
                    locationsArr.append(l.to_dict())
                return BaseResponse(
                        code=0,
                        msg="Locations loaded successfuly",
                        data=locationsArr
                    ).to_dict()
            else:
                resultSet = db_session.query(Location).get(locationId)
                if(resultSet is not None):
                    location = Location.from_dict(resultSet.__dict__)
                    location.id = locationId
                    return BaseResponse(
                            code=0,
                            msg="Location loaded successfuly",
                            data=location.to_dict()
                        ).to_dict()
                else:
                    return BaseResponse(
                            code=1,
                            msg="Location doesn't exists"
                        ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="An error ocurred"
            ).to_dict()
            
    elif request.method == "PUT":
        try:
            resultSet = db_session.query(Location).get(locationId)
            if(resultSet is not None):
                jsonBody = request.get_json()
                locationVal = Location.from_dict(jsonBody)
                location = db_session.query(Location).filter(Location.id == locationId).one()
                location.direction = locationVal.direction
                location.latitude = locationVal.latitude
                location.longitude = locationVal.longitude
                location.branch_office = locationVal.branch_office
                db_session.commit()
                return BaseResponse(
                        code=0,
                        msg="Location updated successfuly",
                        data=location.to_dict()
                    ).to_dict()
            else:
                return BaseResponse(
                        code=1,
                        msg="Location doesn't exists"
                    ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Location couldn't be updated"
                ).to_dict()
        
    elif request.method == "DELETE":
        try:
            db_session.query(Location).filter(Location.id == locationId).delete()
            db_session.commit()
            return BaseResponse(
                code=0,
                msg="Location deleted succesfully"
            ).to_dict()
        except exc.IntegrityError:
            return BaseResponse(
                code=1,
                msg="Location has more related data, delete those data first"
            ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Location couldn't be deleted"
            ).to_dict()
