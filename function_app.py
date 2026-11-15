import azure.functions as func
import logging

from prediction import make_prediction

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="prediction")
def prediction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    tenure = req.params.get('tenure')
    monthly = req.params.get('monthly')
    techsupport = req.params.get('techsupport')

    prediction = make_prediction(
    tenure=float(tenure),
    MonthlyCharges=float(monthly),
    TechSupport_yes=float(techsupport),
                )

    if tenure and monthly and techsupport:
        return func.HttpResponse(f"Hello,the probability of this customer churning is  {prediction}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a tenure, monthly, techsupport in the query string or in the request body for a personalized response.",
             status_code=200
        )