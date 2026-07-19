class ReportGenerator:

    @staticmethod
    def generate(
        probability,
        risk,
        recommendation
    ):
        return (
            f"Failure Probability: {probability:.2f}%\n"
            f"Risk: {risk}\n"
            f"Recommendation: {recommendation}"
        )