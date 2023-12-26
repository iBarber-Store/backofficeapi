from flask import request
from app.api.product import product_bp
from app.model.common.base_response import BaseResponse
from app.model.database.product import Product
from app.config.database import db_session
from sqlalchemy import exc

@product_bp.route("/product", methods=["GET", "POST"])
@product_bp.route("/product/<int:productId>", methods=["GET", "PUT", "DELETE"])
def productAdmin(productId=None):
    if request.method == "POST":
        try:
            jsonBody = request.get_json()
            b = Product.from_dict(jsonBody)
            del b.id
            db_session.add(b)
            db_session.commit()
            return BaseResponse(
                code=0,
                msg="Product created successfuly",
                data=b.to_dict()
            ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Product couldn't be saved"
            ).to_dict()
    
    elif request.method == "GET":
        try:
            if productId is None:
                products = Product.query.all()
                productsArr = []
                for p in products:
                    productsArr.append(p.to_dict())
                return BaseResponse(
                        code=0,
                        msg="Products loaded successfuly",
                        data=productsArr
                    ).to_dict()
            else:
                resultSet = db_session.query(Product).get(productId)
                if(resultSet is not None):
                    product = Product.from_dict(resultSet.__dict__)
                    product.id = productId
                    return BaseResponse(
                            code=0,
                            msg="Product loaded successfuly",
                            data=product.to_dict()
                        ).to_dict()
                else:
                    return BaseResponse(
                            code=1,
                            msg="Product doesn't exists"
                        ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="An error ocurred"
            ).to_dict()
            
    elif request.method == "PUT":
        try:
            resultSet = db_session.query(Product).get(productId)
            if(resultSet is not None):
                jsonBody = request.get_json()
                productVal = Product.from_dict(jsonBody)
                product = db_session.query(Product).filter(Product.id == productId).one()
                product.name = productVal.name
                product.description = productVal.description
                product.schedule = productVal.schedule
                product.branch_office = productVal.branch_office
                db_session.commit()
                return BaseResponse(
                        code=0,
                        msg="Product updated successfuly",
                        data=product.to_dict()
                    ).to_dict()
            else:
                return BaseResponse(
                        code=1,
                        msg="Product doesn't exists"
                    ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Product couldn't be updated"
                ).to_dict()
        
    elif request.method == "DELETE":
        try:
            db_session.query(Product).filter(Product.id == productId).delete()
            db_session.commit()
            return BaseResponse(
                code=0,
                msg="Product deleted succesfully"
            ).to_dict()
        except exc.IntegrityError:
            return BaseResponse(
                code=1,
                msg="Product has more related data, delete those data first"
            ).to_dict()
        except:
            return BaseResponse(
                code=8,
                msg="Product couldn't be deleted"
            ).to_dict()
