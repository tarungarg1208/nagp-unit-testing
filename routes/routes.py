"""Module for trader routes API."""
from datetime import datetime
from os import path
from flask import jsonify
# from flask_restplus import Namespace, Resource
from flask_restx import Namespace, Resource
from webargs.fields import String, Integer, Float
from marshmallow.validate import Length,Range

from utility import PARSER, utils
from handler.trade import Trader

NS_TRADER = Namespace("trader/<user_id>", description="Trader request related routes")

# Creating Trader Object
trader=Trader()


@NS_TRADER.route("/buy/<equity_name>/quantity/<qty>")
class BuyEquity(Resource):
    """Class containing routes for buying equity"""

    @PARSER.use_kwargs(
        dict(
            user_id=String(required=True, validate=Length(1)),
            equity_name=String(required=True, validate=Length(1)),
            qty=Integer(required=True),
        ),
        location="path",
    )
    def post(self, **kwargs):
        """Returns reponse for buy request"""
        user_id=kwargs['user_id']
        equity_name=kwargs['equity_name']
        qty_ordered=kwargs['qty']
        print(f"BUY ORDER INITIATED for user:{user_id}, equity:{equity_name} for QUANTITY:{qty_ordered}")
        response=trader.buy_equity(user_id=user_id,equity_id=equity_name,quantity=qty_ordered)
        return jsonify(response)

@NS_TRADER.route("/sell/<equity_name>/quantity/<qty>")
class SellEquity(Resource):
    """Class containing routes for selling equity"""

    @PARSER.use_kwargs(
        dict(
            user_id=String(required=True, validate=Length(1)),
            equity_name=String(required=True, validate=Length(1)),
            qty=Integer(required=True),
        ),
        location="path",
    )
    def post(self, **kwargs):
        """Returns reponse for sell request"""
        user_id=kwargs['user_id']
        equity_name=kwargs['equity_name']
        qty_ordered=kwargs['qty']
        print(f"BUY SELL INITIATED for user:{user_id}, equity:{equity_name} for QUANTITY:{qty_ordered}")
        response=trader.sell_equity(user_id=user_id, equity_id=equity_name,quantity=qty_ordered)
        return jsonify(response)


@NS_TRADER.route("/fund/<amount>")
class Fund(Resource):
    """Class containing routes for adding funds to user balance"""

    @PARSER.use_kwargs(
        dict(
            user_id=String(required=True, validate=Length(1)),
            amount=Float(required=True, validate=Range(min=0))
        ),
        location="path",
    )
    def post(self, **kwargs):
        """Returns reponse for add fund request"""
        user_id=kwargs['user_id']
        amount_requested=kwargs['amount']
        print(f"ADD AMOUNT REQUEST INITIATED for user:{user_id},AMOUNT:{amount_requested}")
        return jsonify(trader.add_funds(user_id=user_id,amount=amount_requested))

@NS_TRADER.route("")
class User(Resource):
    """Class containing routes for getting user information"""   
    
    @PARSER.use_kwargs(
        dict(
            user_id=String(required=True, validate=Length(1))
        ),
        location="path",
    )
    def get(self, **kwargs):
        """Returns reponse for get_user_info request"""
        user_id=kwargs['user_id']
        print(f"GETTING USER INFO. for user:{user_id}")
        return jsonify(trader.get_user_info(user_id=user_id))
