
import DBConnection as db
import SprintReviewProcess as proc

def getEmployeeReview(empId):
    reviewData = db.getEmployeeReviewDetails(empId)
    processedData = proc.ReviewData(reviewData)
    return processedData.review()