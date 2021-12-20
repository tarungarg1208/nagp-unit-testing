"""Module for trader routes API."""
from datetime import datetime
from os import path
from flask import jsonify
# from flask_restplus import Namespace, Resource
from flask_restx import Namespace, Resource
from webargs.fields import String, Integer
from marshmallow.validate import Length

from utility import PARSER, utils
from handler.trade import Trader

NS_TRADER = Namespace("trader", description="Trader request related routes")

# Creating Trader Object
trader=Trader()


@NS_TRADER.route("/buy/<equity_name>/quantity/<qty>")
class BuyEquity(Resource):
    """Class containing routes for buying equity"""

    @PARSER.use_kwargs(
        dict(
            equity_name=String(required=True, validate=Length(1)),
            qty=Integer(required=True),
        ),
        location="path",
    )
    def post(self, **kwargs):
        """Returns reponse for buy request"""
        equity_name=kwargs['equity_name']
        qty_ordered=kwargs['qty']
        print(f"BUY ORDER INITIATED:{equity_name} for QUANTITY:{qty_ordered}")
        trader.buy_equity(equity=equity_name,quantity=qty_ordered)
        return dict(status="healthy", time=str(datetime.now()), version='v1')

@NS_TRADER.route("/sell/<equity_name>/quantity/<qty>")
class SellEquity(Resource):
    """Class containing routes for selling equity"""

    @PARSER.use_kwargs(
        dict(
            equity_name=String(required=True, validate=Length(1)),
            qty=Integer(required=True),
        ),
        location="path",
    )
    def post(self, **kwargs):
        """Returns reponse for sell request"""
        equity_name=kwargs['equity_name']
        qty_ordered=kwargs['qty']
        print(f"SELL ORDER INITIATED:{equity_name} for QUANTITY:{qty_ordered}")
        trader.sell_equity(equity=equity_name,quantity=qty_ordered)
        return dict(status="healthy", time=str(datetime.now()), version='v1')


@NS_TRADER.route("/fund/<amount>")
class Fund(Resource):
    """Class containing routes for selling equity"""

    @PARSER.use_kwargs(
        dict(
            amount=String(required=True, validate=Length(1))
        ),
        location="path",
    )
    def post(self, **kwargs):
        """Returns reponse for add fund request"""
        amount_requested=kwargs['amount']
        print(f"ADD FUND INITIATED:{amount_requested}")
        
        return jsonify(trader.add_funds(amount=amount_requested))
