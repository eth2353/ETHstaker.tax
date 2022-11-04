from typing import Any, Dict, List, Optional
import datetime

from pydantic import BaseModel, Field


class BalanceAtSlot(BaseModel):
    date: datetime.date = Field(..., example=datetime.date.fromisoformat("2020-01-31"))
    slot: int = Field(..., example=78391)
    balance: float = Field(..., example=32.42)


class EndOfDayBalance(BalanceAtSlot):
    pass


class ErrorMessage(BaseModel):
    message: str = Field(..., example="No data found for the provided input.")


class InitialBalance(BalanceAtSlot):
    pass


class ValidatorRewards(BaseModel):
    validator_index: int = Field(..., example=1234)
    # This field is optional - if a validator has not been active in the requested
    # time period, it will be set to None
    initial_balance: Optional[InitialBalance]
    eod_balances: List[EndOfDayBalance]
    total_eth: float = Field(..., example=12.456, description="Total rewards in ETH.")
    total_currency: float = Field(
        ..., example=12456.78, description="Total rewards in the requested currency."
    )


class AggregateRewards(BaseModel):
    validator_rewards: List[ValidatorRewards]
    currency: str = Field(..., example="EUR")
    eth_prices: Dict = Field(..., example={"2021-01-01": 502.4, "2021-01-02": 554.32})


class DataForEpoch(BaseModel):
    indexes_missing: int
    indexes_timely_source: int
    indexes_timely_target: int
    indexes_timely_head: int


class IndexedMergeData(BaseModel):
    __root__: Dict[int, DataForEpoch]


class ValidatorInclusionEpochData(BaseModel):
    current_epoch_active_gwei: int
    current_epoch_target_attesting_gwei: int

    previous_epoch_active_gwei: int
    previous_epoch_target_attesting_gwei: int
    previous_epoch_head_attesting_gwei: int


class ValidatorInclusionData(BaseModel):
    __root__: Dict[int, ValidatorInclusionEpochData]
