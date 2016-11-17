#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = [
        (age, net_worth, calculate_residual_error(prediction, net_worth))
        for (prediction, age, net_worth) in zip(predictions, ages, net_worths)
    ]
    to_pick = int(len(ages) * 0.9)
    return sorted(cleaned_data, key=lambda c: c[-1])[:to_pick]


def calculate_residual_error(prediction, net_worth):
    return prediction*prediction - net_worth*net_worth
