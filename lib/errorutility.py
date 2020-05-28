from rest_framework import status
from rest_framework.response import Response
from lib import constants as const
from lib import errormessages as errorMessages

def getInternalServerErrorResponse():
	return Response(
		{const.ERROR_PROPERTY : errorMessages.INTERNAL_SERVER_ERROR},
		status=status.HTTP_500_INTERNAL_SERVER_ERROR
	)
