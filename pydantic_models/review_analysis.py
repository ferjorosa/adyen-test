from pydantic import BaseModel, Field
from typing import List, Tuple, Optional


class ReviewAnalysis(BaseModel):
    safety_issues: Tuple[bool, Optional[str]] = Field(
        ...,
        description="A tuple indicating whether there are safety issues (True/False) and an explanation of the issues if present."
    )

    most_appreciated_features: List[str] = Field(
        ...,
        description="A list of features that customers frequently appreciate."
    )

    least_appreciated_features: List[str] = Field(
        ...,
        description="A list of features that customers criticize."
    )

    price_evaluation: Tuple[bool, str] = Field(
        ...,
        description="A tuple indicating whether the price is acceptable (True/False) and an explanation regarding the pricing."
    )

    shipping_evaluation: Tuple[bool, str] = Field(
        ...,
        description="A tuple indicating whether the shipping experience was satisfactory (True/False) and an explanation of the shipping details."
    )

    return_process_evaluation: Tuple[bool, Optional[str]] = Field(
        ...,
        description="A tuple indicating whether any products were returned (True/False) and an explanation of the return process if applicable."
    )

    mentions_of_competing_products: Tuple[bool, Optional[str]] = Field(
        ...,
        description="A tuple indicating whether there are mentions of competing products (True/False) and an explanation of those mentions if present."
    )


if __name__ == "__main__":

    # Example of how to use this model
    analysis = ReviewAnalysis(
        safety_issues=(True, "Choking hazard due to small parts."),
        most_appreciated_features=["Easy to clean", "Sturdy construction"],
        least_appreciated_features=["Bulky design", "Difficult to assemble"],
        price_evaluation=(True, "Most customers find the price reasonable for the quality."),
        shipping_evaluation=(True, "Fast and reliable shipping reported by customers."),
        return_process_evaluation=(False, None),  # No significant mentions of returns
        mentions_of_competing_products=(True, "Competitors like Brand X are mentioned for better durability.")
    )

    print(analysis.model_dump_json(indent=4))  # Print the analysis in JSON format
