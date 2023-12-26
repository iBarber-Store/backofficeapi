from flask import request
from app.api.price import price_bp
from app.model.common.base_response import BaseResponse
from app.model.database.price import Price
from app.config.database import db_session
from sqlalchemy import exc

@price_bp.route("/price", methods=["GET", "POST"])
@price_bp.route("/price/<int:priceId>", methods=["GET", "PUT", "DELETE"])
def priceAdmin(priceId=None):
    if request.method == "POST":
        try:
            jsonBody = request.get_json()
            p = Price.from_dict(jsonBody)
            del p.id
            db_session.add(p)
            db_session.commit()
            return BaseResponse(
                code=0,
                msg="Price created successfuly",
                data=p.to_dict()
            ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Price couldn't be saved"
            ).to_dict()
    
    elif request.method == "GET":
        try:
            if priceId is None:
                prices = Price.query.all()
                pricesArr = []
                for p in prices:
                    pricesArr.append(p.to_dict())
                return BaseResponse(
                        code=0,
                        msg="Prices loaded successfuly",
                        data=pricesArr
                    ).to_dict()
            else:
                resultSet = db_session.query(Price).get(priceId)
                if(resultSet is not None):
                    price = Price.from_dict(resultSet.__dict__)
                    price.id = priceId
                    return BaseResponse(
                            code=0,
                            msg="Price loaded successfuly",
                            data=price.to_dict()
                        ).to_dict()
                else:
                    return BaseResponse(
                            code=1,
                            msg="Price doesn't exists"
                        ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="An error ocurred"
            ).to_dict()
            
    elif request.method == "PUT":
        try:
            resultSet = db_session.query(Price).get(priceId)
            if(resultSet is not None):
                jsonBody = request.get_json()
                priceVal = Price.from_dict(jsonBody)
                price = db_session.query(Price).filter(Price.id == priceId).one()
                price.product = priceVal.product
                price.price = priceVal.price
                price.price_full = priceVal.price_full
                db_session.commit()
                return BaseResponse(
                        code=0,
                        msg="Price updated successfuly",
                        data=price.to_dict()
                    ).to_dict()
            else:
                return BaseResponse(
                        code=1,
                        msg="Price doesn't exists"
                    ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Price couldn't be updated"
                ).to_dict()
        
    elif request.method == "DELETE":
        try:
            db_session.query(Price).filter(Price.id == priceId).delete()
            db_session.commit()
            return BaseResponse(
                code=0,
                msg="Price deleted succesfully"
            ).to_dict()
        except exc.IntegrityError:
            return BaseResponse(
                code=1,
                msg="Price has more related data, delete those data first"
            ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Price couldn't be deleted"
            ).to_dict()
