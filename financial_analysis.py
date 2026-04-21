{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0eb657d9-f509-4094-81be-82e5a2ad234d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--- Project Financial Analysis ---\n",
      "Cash Flows and Present Values:\n",
      "|   Year |   Cash_Flow_kUSD |   Present_Value_kUSD |\n",
      "|-------:|-----------------:|---------------------:|\n",
      "|      0 |             -500 |            -500      |\n",
      "|      1 |              150 |             130.435  |\n",
      "|      2 |              200 |             151.229  |\n",
      "|      3 |              200 |             131.503  |\n",
      "|      4 |              150 |              85.763  |\n",
      "|      5 |              100 |              49.7177 |\n",
      "\n",
      "Discount Rate: 15%\n",
      "Calculated Net Present Value (NPV): $48.65 kUSD\n",
      "\n",
      "Decision: The project is expected to be profitable (NPV > 0) and should be accepted as it adds value.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "DISCOUNT_RATE = 0.15 # 15%\n",
    "# --- STEP 1: To calculate the cash flow in kUSD\n",
    "project_data = {\n",
    "    'Year': [0, 1, 2, 3, 4, 5],\n",
    "    'Cash_Flow_kUSD': [-500, 150, 200, 200, 150, 100]\n",
    "}\n",
    "df = pd.DataFrame(project_data)\n",
    "\n",
    "# --- STEP 2: Calculate Present Value (PV) of each Cash Flow ---\n",
    "# PV Formula: Cash_Flow / (1 + Discount_Rate)^Year\n",
    "def calculate_pv(row, rate):\n",
    "    \"\"\"Calculates the present value for a given cash flow and year.\"\"\"\n",
    "    year = row['Year']\n",
    "    cash_flow = row['Cash_Flow_kUSD']\n",
    "    if year == 0:\n",
    "        return cash_flow # Initial investment is already at present value\n",
    "    else:\n",
    "        return cash_flow / ((1 + rate) ** year)\n",
    "\n",
    "df['Present_Value_kUSD'] = df.apply(lambda row: calculate_pv(row, DISCOUNT_RATE), axis=1)\n",
    "\n",
    "# --- STEP 3: Calculate Net Present Value (NPV) ---\n",
    "# NPV is the sum of all Present Values.\n",
    "npv = df['Present_Value_kUSD'].sum()\n",
    "\n",
    "# --- STEP 4: Display Results ---\n",
    "print(\"--- Project Financial Analysis ---\")\n",
    "print(\"Cash Flows and Present Values:\")\n",
    "print(df.to_markdown(index=False)) # Using to_markdown for neat output in a notebook\n",
    "print(f\"\\nDiscount Rate: {DISCOUNT_RATE * 100:.0f}%\")\n",
    "print(f\"Calculated Net Present Value (NPV): ${npv:.2f} kUSD\")\n",
    "\n",
    "# --- STEP 5: Business Decision Rule ---\n",
    "if npv > 0:\n",
    "    print(\"\\nDecision: The project is expected to be profitable (NPV > 0) and should be accepted as it adds value.\")\n",
    "else:\n",
    "    print(\"\\nDecision: The project is not expected to be profitable (NPV <= 0) and should be rejected.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b246ece6-c9f9-4282-9b0d-c2293bda3757",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting numpy-financial\n",
      "  Using cached numpy_financial-1.0.0-py3-none-any.whl.metadata (2.2 kB)\n",
      "Requirement already satisfied: numpy>=1.15 in .\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages (from numpy-financial) (2.4.2)\n",
      "Using cached numpy_financial-1.0.0-py3-none-any.whl (14 kB)\n",
      "Installing collected packages: numpy-financial\n",
      "Successfully installed numpy-financial-1.0.0\n"
     ]
    }
   ],
   "source": [
    "!pip install numpy-financial"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3f3f8677-fc39-4021-97a3-a638cbb7ba6a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--- Project Financial Analysis (10-Year Horizon) ---\n",
      "Discount Rate (Required Return): 10%\n",
      "\n",
      "Detailed Cash Flows and Present Values:\n",
      "|   Year |   Cash_Flow_kUSD |   Discount_Factor |   Present_Value_kUSD |\n",
      "|-------:|-----------------:|------------------:|---------------------:|\n",
      "|      0 |         -1000.00 |            1.0000 |             -1000.00 |\n",
      "|      1 |           250.00 |            0.9091 |               227.27 |\n",
      "|      2 |           350.00 |            0.8264 |               289.26 |\n",
      "|      3 |           400.00 |            0.7513 |               300.53 |\n",
      "|      4 |           300.00 |            0.6830 |               204.90 |\n",
      "|      5 |           300.00 |            0.6209 |               186.28 |\n",
      "|      6 |           250.00 |            0.5645 |               141.12 |\n",
      "|      7 |           200.00 |            0.5132 |               102.63 |\n",
      "|      8 |           150.00 |            0.4665 |                69.98 |\n",
      "|      9 |           100.00 |            0.4241 |                42.41 |\n",
      "|     10 |            50.00 |            0.3855 |                19.28 |\n",
      "\n",
      "Total Net Present Value (NPV): $742.01 kUSD\n",
      "Internal Rate of Return (IRR): 25.05%\n",
      "\n",
      "--- Project Decision and Insights ---\n",
      "\n",
      "NPV Conclusion: **ACCEPT** - The project is expected to generate value (NPV > 0).\n",
      "IRR Conclusion: **ACCEPT** - The project's return (25.05%) exceeds the required return (10%).\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy_financial as npf # Standard library for financial calculations\n",
    "import numpy as np\n",
    "\n",
    "# --- STEP 1: Define Project Parameters (10-Year Horizon) ---\n",
    "DISCOUNT_RATE = 0.10 # WACC or required rate of return (10%)\n",
    "\n",
    "# Cash flows for the project over 10 years (11 entries total)\n",
    "# Year 0 is the initial investment (negative cash flow). Values are in thousands of dollars (kUSD).\n",
    "# This structure simulates phases: Investment -> High Growth -> Maturity -> Decline\n",
    "CASH_FLOWS_kUSD = np.array([\n",
    "    -1000, # Year 0: Initial Investment\n",
    "    250,   # Year 1: High Growth\n",
    "    350,   # Year 2: High Growth\n",
    "    400,   # Year 3: High Growth\n",
    "    300,   # Year 4: Maturity\n",
    "    300,   # Year 5: Maturity\n",
    "    250,   # Year 6: Maturity\n",
    "    200,   # Year 7: Decline Start\n",
    "    150,   # Year 8: Decline\n",
    "    100,   # Year 9: Decline\n",
    "    50     # Year 10: Wind Down / Salvage Value\n",
    "])\n",
    "PROJECT_LENGTH = len(CASH_FLOWS_kUSD) - 1\n",
    "\n",
    "# --- STEP 2: Create DataFrame for Detailed Analysis ---\n",
    "df = pd.DataFrame({\n",
    "    'Year': np.arange(PROJECT_LENGTH + 1),\n",
    "    'Cash_Flow_kUSD': CASH_FLOWS_kUSD\n",
    "})\n",
    "\n",
    "# --- STEP 3: Calculate Present Value (PV) of each Cash Flow (Manual for detail) ---\n",
    "# PV Formula: Cash_Flow / (1 + Discount_Rate)^Year\n",
    "def calculate_pv(row, rate):\n",
    "    \"\"\"Calculates the present value for a given cash flow and year.\"\"\"\n",
    "    year = row['Year']\n",
    "    cash_flow = row['Cash_Flow_kUSD']\n",
    "    # The discount factor is 1 / (1 + rate)^year\n",
    "    discount_factor = 1 / ((1 + rate) ** year)\n",
    "    present_value = cash_flow * discount_factor\n",
    "    return present_value\n",
    "\n",
    "df['Present_Value_kUSD'] = df.apply(lambda row: calculate_pv(row, DISCOUNT_RATE), axis=1)\n",
    "df['Discount_Factor'] = df.apply(lambda row: 1 / ((1 + DISCOUNT_RATE) ** row['Year']), axis=1).round(4)\n",
    "\n",
    "\n",
    "# --- STEP 4: Calculate Key Metrics using numpy_financial ---\n",
    "# NPV: Net Present Value (Total PV of all future cash flows, plus the initial investment)\n",
    "# Note: npf.npv calculates the PV of the *list*, excluding the first value, so we add it back.\n",
    "npv_result = npf.npv(DISCOUNT_RATE, CASH_FLOWS_kUSD[1:]) + CASH_FLOWS_kUSD[0]\n",
    "\n",
    "# IRR: Internal Rate of Return (The rate at which NPV equals zero)\n",
    "irr_result = npf.irr(CASH_FLOWS_kUSD)\n",
    "\n",
    "\n",
    "# --- STEP 5: Display Comprehensive Results ---\n",
    "print(f\"--- Project Financial Analysis (10-Year Horizon) ---\")\n",
    "print(f\"Discount Rate (Required Return): {DISCOUNT_RATE * 100:.0f}%\")\n",
    "\n",
    "print(\"\\nDetailed Cash Flows and Present Values:\")\n",
    "# Displaying the results with Markdown for clean Jupyter output\n",
    "print(df[['Year', 'Cash_Flow_kUSD', 'Discount_Factor', 'Present_Value_kUSD']].to_markdown(index=False, floatfmt=(\".0f\", \".2f\", \".4f\", \".2f\")))\n",
    "\n",
    "print(f\"\\nTotal Net Present Value (NPV): ${npv_result:,.2f} kUSD\")\n",
    "print(f\"Internal Rate of Return (IRR): {irr_result * 100:.2f}%\")\n",
    "\n",
    "print(\"\\n--- Project Decision and Insights ---\")\n",
    "if npv_result > 0:\n",
    "    npv_decision = \"ACCEPT\"\n",
    "    npv_reason = \"The project is expected to generate value (NPV > 0).\"\n",
    "else:\n",
    "    npv_decision = \"REJECT\"\n",
    "    npv_reason = \"The project is not expected to generate value (NPV <= 0).\"\n",
    "\n",
    "if irr_result > DISCOUNT_RATE:\n",
    "    irr_decision = \"ACCEPT\"\n",
    "    irr_reason = \"The project's return ({:.2f}%) exceeds the required return ({:.0f}%).\".format(irr_result * 100, DISCOUNT_RATE * 100)\n",
    "else:\n",
    "    irr_decision = \"REJECT\"\n",
    "    irr_reason = \"The project's return ({:.2f}%) is less than the required return ({:.0f}%).\".format(irr_result * 100, DISCOUNT_RATE * 100)\n",
    "\n",
    "print(f\"\\nNPV Conclusion: **{npv_decision}** - {npv_reason}\")\n",
    "print(f\"IRR Conclusion: **{irr_decision}** - {irr_reason}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "95c9dbb3-b272-4dd0-aaac-ba28934d4190",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Project Cash Flows: [-500  150  200  200  150  100]\n",
      "Required Discount Rate: 15%\n",
      "\n",
      "--- Project Financial Analysis ---\n",
      "\n",
      "Cash Flows and Present Values:\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Year</th>\n",
       "      <th>Cash_Flow ($)</th>\n",
       "      <th>Present_Value ($)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>$-500</td>\n",
       "      <td>$-500.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>$150</td>\n",
       "      <td>$130.43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>$200</td>\n",
       "      <td>$151.23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>$200</td>\n",
       "      <td>$131.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>$150</td>\n",
       "      <td>$85.76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>5</td>\n",
       "      <td>$100</td>\n",
       "      <td>$49.72</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Year Cash_Flow ($) Present_Value ($)\n",
       "0     0         $-500          $-500.00\n",
       "1     1          $150           $130.43\n",
       "2     2          $200           $151.23\n",
       "3     3          $200           $131.50\n",
       "4     4          $150            $85.76\n",
       "5     5          $100            $49.72"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Discount Rate: 15%\n",
      "Calculated Net Present Value (NPV): **$130.94**\n",
      "Calculated Internal Rate of Return (IRR): **19.25%**\n",
      "\n",
      "NPV Conclusion: **ACCEPT** - The project is expected to generate value (NPV > 0).\n",
      "IRR Conclusion: **ACCEPT** - The project's return (19.25%) exceeds the required return (15%).\n"
     ]
    }
   ],
   "source": [
    "# Import necessary libraries\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "from IPython.display import display\n",
    "# NEW IMPORT: numpy_financial for NPV and IRR\n",
    "import numpy_financial as npf\n",
    "\n",
    "# --- Project Data ---\n",
    "# Cash flows (initial investment in year 0 is negative, followed by inflows)\n",
    "CASH_FLOWS = np.array([-500, 150, 200, 200, 150, 100])\n",
    "# Required rate of return (Discount Rate) as a decimal\n",
    "DISCOUNT_RATE = 0.15\n",
    "\n",
    "print('Project Cash Flows:', CASH_FLOWS)\n",
    "print('Required Discount Rate: {:.0f}%'.format(DISCOUNT_RATE * 100))\n",
    "\n",
    "# --- NPV & IRR Calculation ---\n",
    "def calculate_present_value(cash_flow, rate, year):\n",
    "    # Calculates the present value of a single cash flow: CF / (1 + r)^n\n",
    "    return cash_flow / (1 + rate)**year\n",
    "\n",
    "# 1. Calculate Net Present Value (NPV)\n",
    "# CORRECTED: Using npf.npv instead of np.npv\n",
    "npv_result = npf.npv(DISCOUNT_RATE, CASH_FLOWS[1:]) + CASH_FLOWS[0]\n",
    "\n",
    "# 2. Calculate Internal Rate of Return (IRR)\n",
    "# CORRECTED: Using npf.irr instead of np.irr\n",
    "irr_result = npf.irr(CASH_FLOWS)\n",
    "\n",
    "# --- Display Results ---\n",
    "print('\\n--- Project Financial Analysis ---')\n",
    "\n",
    "# Prepare detailed breakdown table\n",
    "years = np.arange(len(CASH_FLOWS))\n",
    "pv_flows = [calculate_present_value(cf, DISCOUNT_RATE, y) for cf, y in zip(CASH_FLOWS, years)]\n",
    "\n",
    "df = pd.DataFrame({\n",
    "    'Year': years,\n",
    "    'Cash_Flow ($)': CASH_FLOWS,\n",
    "    'Present_Value ($)': pv_flows\n",
    "})\n",
    "\n",
    "# Formatting for clear display\n",
    "df['Cash_Flow ($)'] = df['Cash_Flow ($)'].map('${:,.0f}'.format)\n",
    "df['Present_Value ($)'] = df['Present_Value ($)'].map('${:,.2f}'.format)\n",
    "\n",
    "print('\\nCash Flows and Present Values:')\n",
    "display(df)\n",
    "\n",
    "print(f'\\nDiscount Rate: {DISCOUNT_RATE * 100:.0f}%')\n",
    "print(f'Calculated Net Present Value (NPV): **${npv_result:.2f}**')\n",
    "print(f'Calculated Internal Rate of Return (IRR): **{irr_result * 100:.2f}%**')\n",
    "\n",
    "# --- Investment Decision Rules ---\n",
    "\n",
    "# NPV Rule: Accept if NPV > 0\n",
    "if npv_result > 0:\n",
    "    npv_decision = \"ACCEPT\"\n",
    "    npv_reason = \"The project is expected to generate value (NPV > 0).\"\n",
    "else:\n",
    "    npv_decision = \"REJECT\"\n",
    "    npv_reason = \"The project is not expected to generate value (NPV <= 0).\"\n",
    "\n",
    "# IRR Rule: Accept if IRR > Discount Rate\n",
    "if irr_result > DISCOUNT_RATE:\n",
    "    irr_decision = \"ACCEPT\"\n",
    "    irr_reason = f\"The project's return ({irr_result * 100:.2f}%) exceeds the required return ({DISCOUNT_RATE * 100:.0f}%).\"\n",
    "else:\n",
    "    irr_decision = \"REJECT\"\n",
    "    irr_reason = f\"The project's return ({irr_result * 100:.2f}%) is less than the required return ({DISCOUNT_RATE * 100:.0f}%).\"\n",
    "\n",
    "print(f\"\\nNPV Conclusion: **{npv_decision}** - {npv_reason}\")\n",
    "print(f\"IRR Conclusion: **{irr_decision}** - {irr_reason}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c3342b0d-1157-48c3-9b6c-0c7bdcabd910",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting plotly\n",
      "  Downloading plotly-6.7.0-py3-none-any.whl.metadata (8.6 kB)\n",
      "Requirement already satisfied: narwhals>=1.15.1 in .\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages (from plotly) (2.18.1)\n",
      "Requirement already satisfied: packaging in .\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages (from plotly) (26.0)\n",
      "Downloading plotly-6.7.0-py3-none-any.whl (9.9 MB)\n",
      "   ---------------------------------------- 0.0/9.9 MB ? eta -:--:--\n",
      "   ---------------------------------------- 0.0/9.9 MB ? eta -:--:--\n",
      "   - -------------------------------------- 0.3/9.9 MB ? eta -:--:--\n",
      "   ---- ----------------------------------- 1.0/9.9 MB 2.8 MB/s eta 0:00:04\n",
      "   ------ --------------------------------- 1.6/9.9 MB 2.8 MB/s eta 0:00:03\n",
      "   ----------- ---------------------------- 2.9/9.9 MB 3.6 MB/s eta 0:00:02\n",
      "   ---------------- ----------------------- 4.2/9.9 MB 4.1 MB/s eta 0:00:02\n",
      "   ----------------------- ---------------- 5.8/9.9 MB 4.8 MB/s eta 0:00:01\n",
      "   ----------------------------- ---------- 7.3/9.9 MB 5.1 MB/s eta 0:00:01\n",
      "   ---------------------------------------  9.7/9.9 MB 5.9 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 9.9/9.9 MB 5.8 MB/s  0:00:01\n",
      "Installing collected packages: plotly\n",
      "Successfully installed plotly-6.7.0\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install plotly"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "72f90020-d9fc-4724-b202-5a23ff89149b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "# Project Alpha Analysis"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hole": 0.6,
         "labels": [
          "IRR Premium",
          "Hurdle Rate"
         ],
         "marker": {
          "colors": [
           "#0088C8",
           "#78D0ED"
          ]
         },
         "type": "pie",
         "values": [
          0.1505,
          0.1
         ]
        }
       ],
       "layout": {
        "annotations": [
         {
          "showarrow": false,
          "text": "25.05% IRR",
          "x": 0.5,
          "y": 0.5
         }
        ],
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermap": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermap"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "IRR vs Hurdle Rate"
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "marker": {
          "color": [
           "red",
           "blue",
           "blue",
           "blue",
           "blue",
           "blue",
           "blue",
           "blue",
           "blue",
           "blue",
           "blue"
          ]
         },
         "type": "bar",
         "x": {
          "bdata": "AAECAwQFBgcICQo=",
          "dtype": "i1"
         },
         "y": {
          "bdata": "GPz6AF4BkAEsASwB+gDIAJYAZAAyAA==",
          "dtype": "i2"
         }
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermap": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermap"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Cash Flow Over Time"
        },
        "xaxis": {
         "title": {
          "text": "Year"
         }
        },
        "yaxis": {
         "title": {
          "text": "Cash Flow"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "name": "High Growth (Y 1-3)",
         "orientation": "h",
         "type": "bar",
         "x": [
          817.06
         ],
         "y": [
          "PV Contribution"
         ]
        },
        {
         "name": "Maturity (Y 4-6)",
         "orientation": "h",
         "type": "bar",
         "x": [
          532.3
         ],
         "y": [
          "PV Contribution"
         ]
        },
        {
         "name": "Decline (Y 7-10)",
         "orientation": "h",
         "type": "bar",
         "x": [
          234.29
         ],
         "y": [
          "PV Contribution"
         ]
        }
       ],
       "layout": {
        "barmode": "stack",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermap": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermap"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "PV Contribution by Phase"
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import plotly.graph_objects as go\n",
    "from IPython.display import display, Markdown\n",
    "import numpy_financial as npf\n",
    "\n",
    "# --- Colors ---\n",
    "COLORS = ['#003F63', '#006094', '#0088C8', '#30AADD', '#78D0ED']\n",
    "\n",
    "# --- Cash Flow Data ---\n",
    "CASH_FLOWS = [-1000, 250, 350, 400, 300, 300, 250, 200, 150, 100, 50]\n",
    "YEARS = list(range(len(CASH_FLOWS)))\n",
    "df_cf = pd.DataFrame({'Year': YEARS, 'Cash_Flow': CASH_FLOWS})\n",
    "\n",
    "# --- Phase Data ---\n",
    "df_phase = pd.DataFrame({\n",
    "    'Phase': ['High Growth (Y 1-3)', 'Maturity (Y 4-6)', 'Decline (Y 7-10)'],\n",
    "    'PV_Contribution': [817.06, 532.30, 234.29]\n",
    "})\n",
    "\n",
    "# --- IRR Donut Chart ---\n",
    "def create_irr_donut(irr_percent, hurdle_percent):\n",
    "    irr = irr_percent / 100\n",
    "    hurdle = hurdle_percent / 100\n",
    "    premium = irr - hurdle\n",
    "\n",
    "    fig = go.Figure(data=[\n",
    "        go.Pie(\n",
    "            labels=['IRR Premium', 'Hurdle Rate'],\n",
    "            values=[premium, hurdle],\n",
    "            hole=0.6,\n",
    "            marker_colors=[COLORS[2], COLORS[4]]\n",
    "        )\n",
    "    ])\n",
    "\n",
    "    fig.update_layout(\n",
    "        title='IRR vs Hurdle Rate',\n",
    "        annotations=[dict(text=f'{irr_percent:.2f}% IRR', x=0.5, y=0.5, showarrow=False)]\n",
    "    )\n",
    "\n",
    "    fig.show()\n",
    "\n",
    "# --- Cash Flow Chart ---\n",
    "def create_cash_flow_bar(df):\n",
    "    fig = go.Figure()\n",
    "\n",
    "    fig.add_trace(go.Bar(\n",
    "        x=df['Year'],\n",
    "        y=df['Cash_Flow'],\n",
    "        marker_color=['red' if cf < 0 else 'blue' for cf in df['Cash_Flow']]\n",
    "    ))\n",
    "\n",
    "    fig.update_layout(\n",
    "        title='Cash Flow Over Time',\n",
    "        xaxis_title='Year',\n",
    "        yaxis_title='Cash Flow'\n",
    "    )\n",
    "\n",
    "    fig.show()\n",
    "\n",
    "# --- Phase Contribution ---\n",
    "def create_phase_stack_bar(df):\n",
    "    fig = go.Figure()\n",
    "\n",
    "    for i, row in df.iterrows():\n",
    "        fig.add_trace(go.Bar(\n",
    "            name=row['Phase'],\n",
    "            y=['PV Contribution'],\n",
    "            x=[row['PV_Contribution']],\n",
    "            orientation='h'\n",
    "        ))\n",
    "\n",
    "    fig.update_layout(\n",
    "        barmode='stack',\n",
    "        title='PV Contribution by Phase'\n",
    "    )\n",
    "\n",
    "    fig.show()\n",
    "\n",
    "# --- Execution ---\n",
    "display(Markdown(\"# Project Alpha Analysis\"))\n",
    "\n",
    "create_irr_donut(25.05, 10.00)\n",
    "create_cash_flow_bar(df_cf)\n",
    "create_phase_stack_bar(df_phase)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "6d58aba2-9103-458b-b919-1c65fd682536",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "\n",
       "# Project Alpha: A Data Visualization Infographic\n",
       "\n",
       "## **Recommendation: ACCEPT**\n",
       "\n",
       "This report visualizes the key financial metrics and forecasts for **Project Alpha**, confirming its viability. The project delivers substantial value, evidenced by a high Net Present Value (NPV) and a significant Internal Rate of Return (IRR) that far exceeds the Hurdle Rate (Cost of Capital). \n",
       "\n",
       "---\n",
       "### Core Financial Metrics (Based on 10.00% Hurdle Rate)\n",
       "\n",
       "| Metric | Value | Conclusion |\n",
       "|:---|:---|:---|\n",
       "| **Net Present Value (NPV)** | **$742.01 kUSD** | Expected value generated (NPV > 0) |\n",
       "| **Internal Rate of Return (IRR)** | **25.05%** | Project return exceeds required return |\n",
       "| **Hurdle Rate (Cost of Capital)** | **10.00%** | Benchmark for investment |\n",
       "| **Margin of Safety** | **15.05%** | Robust buffer against risk |\n",
       "\n",
       "---\n",
       "The analysis below deconstructs the 'why' behind this recommendation, focusing on the project's profitability and lifecycle.\n"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "## 1. Margin of Safety Analysis"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "The **25.05% IRR** provides a 15.05 percentage point premium over the **10.00% cost of capital**, demonstrating a strong capacity to absorb risk and maintain profitability. This margin is the foundation of the 'ACCEPT' recommendation."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hole": 0.6,
         "hovertemplate": "%{label}<br>Value: %{percent}<extra></extra>",
         "labels": [
          "IRR Premium (15.05%)",
          "Hurdle Rate (10.00%)"
         ],
         "marker": {
          "colors": [
           "#0088C8",
           "#78D0ED"
          ]
         },
         "name": "",
         "type": "pie",
         "values": {
          "bdata": "yz67h8tEwz+amZmZmZm5Pw==",
          "dtype": "f8"
         }
        }
       ],
       "layout": {
        "annotations": [
         {
          "font": {
           "size": 20
          },
          "showarrow": false,
          "text": "25.05%<br>IRR",
          "x": 0.5,
          "y": 0.5
         }
        ],
        "height": 400,
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "white",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "white",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "#C8D4E3",
             "linecolor": "#C8D4E3",
             "minorgridcolor": "#C8D4E3",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "#C8D4E3",
             "linecolor": "#C8D4E3",
             "minorgridcolor": "#C8D4E3",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermap": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermap"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "white",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "#C8D4E3"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "white",
          "polar": {
           "angularaxis": {
            "gridcolor": "#EBF0F8",
            "linecolor": "#EBF0F8",
            "ticks": ""
           },
           "bgcolor": "white",
           "radialaxis": {
            "gridcolor": "#EBF0F8",
            "linecolor": "#EBF0F8",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           },
           "yaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           },
           "zaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           },
           "bgcolor": "white",
           "caxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "#EBF0F8",
           "linecolor": "#EBF0F8",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#EBF0F8",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "#EBF0F8",
           "linecolor": "#EBF0F8",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#EBF0F8",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "IRR vs. Hurdle Rate: Margin of Safety",
         "x": 0.5
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "## 2. Project Lifecycle & Value Contribution"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "The initial investment (Year 0) is followed by a predictable pattern of returns, peaking in the High Growth phase (Years 1-3) and stabilizing in the Maturity phase (Years 4-6) before a planned wind-down."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "Year %{x}<br>Cash Flow: $%{y:,.0f} kUSD<extra></extra>",
         "marker": {
          "color": [
           "#003F63",
           "#0088C8",
           "#0088C8",
           "#0088C8",
           "#0088C8",
           "#0088C8",
           "#0088C8",
           "#0088C8",
           "#0088C8",
           "#0088C8",
           "#0088C8"
          ]
         },
         "type": "bar",
         "x": {
          "bdata": "AAECAwQFBgcICQo=",
          "dtype": "i1"
         },
         "y": {
          "bdata": "GPz6AF4BkAEsASwB+gDIAJYAZAAyAA==",
          "dtype": "i2"
         }
        }
       ],
       "layout": {
        "height": 500,
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "white",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "white",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "#C8D4E3",
             "linecolor": "#C8D4E3",
             "minorgridcolor": "#C8D4E3",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "#C8D4E3",
             "linecolor": "#C8D4E3",
             "minorgridcolor": "#C8D4E3",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermap": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermap"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "white",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "#C8D4E3"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "white",
          "polar": {
           "angularaxis": {
            "gridcolor": "#EBF0F8",
            "linecolor": "#EBF0F8",
            "ticks": ""
           },
           "bgcolor": "white",
           "radialaxis": {
            "gridcolor": "#EBF0F8",
            "linecolor": "#EBF0F8",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           },
           "yaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           },
           "zaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           },
           "bgcolor": "white",
           "caxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "#EBF0F8",
           "linecolor": "#EBF0F8",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#EBF0F8",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "#EBF0F8",
           "linecolor": "#EBF0F8",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#EBF0F8",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Project Alpha: 10-Year Cash Flow Lifecycle"
        },
        "xaxis": {
         "title": {
          "text": "Project Year"
         }
        },
        "yaxis": {
         "title": {
          "text": "Cash Flow ($ kUSD)"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "### Value Breakdown by Phase"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "The project's value isn't uniform. The **High Growth** phase creates the most significant portion of the total positive present value, rapidly de-risking the initial investment."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "High Growth (Y 1-3): ${x:,.2f} kUSD<extra></extra>",
         "marker": {
          "color": "#003F63"
         },
         "name": "High Growth (Y 1-3)",
         "orientation": "h",
         "type": "bar",
         "x": [
          817.06
         ],
         "y": [
          "PV Contribution"
         ]
        },
        {
         "hovertemplate": "Maturity (Y 4-6): ${x:,.2f} kUSD<extra></extra>",
         "marker": {
          "color": "#006094"
         },
         "name": "Maturity (Y 4-6)",
         "orientation": "h",
         "type": "bar",
         "x": [
          532.3
         ],
         "y": [
          "PV Contribution"
         ]
        },
        {
         "hovertemplate": "Decline (Y 7-10): ${x:,.2f} kUSD<extra></extra>",
         "marker": {
          "color": "#0088C8"
         },
         "name": "Decline (Y 7-10)",
         "orientation": "h",
         "type": "bar",
         "x": [
          234.29
         ],
         "y": [
          "PV Contribution"
         ]
        }
       ],
       "layout": {
        "barmode": "stack",
        "height": 300,
        "legend": {
         "orientation": "h",
         "x": 0.5,
         "xanchor": "center",
         "y": -0.3,
         "yanchor": "bottom"
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "white",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "white",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "#C8D4E3",
             "linecolor": "#C8D4E3",
             "minorgridcolor": "#C8D4E3",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "#C8D4E3",
             "linecolor": "#C8D4E3",
             "minorgridcolor": "#C8D4E3",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermap": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermap"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "white",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "#C8D4E3"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "white",
          "polar": {
           "angularaxis": {
            "gridcolor": "#EBF0F8",
            "linecolor": "#EBF0F8",
            "ticks": ""
           },
           "bgcolor": "white",
           "radialaxis": {
            "gridcolor": "#EBF0F8",
            "linecolor": "#EBF0F8",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           },
           "yaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           },
           "zaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           },
           "bgcolor": "white",
           "caxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "#EBF0F8",
           "linecolor": "#EBF0F8",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#EBF0F8",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "#EBF0F8",
           "linecolor": "#EBF0F8",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#EBF0F8",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Value Deconstruction: PV Contribution by Project Phase"
        },
        "xaxis": {
         "title": {
          "text": "Present Value ($ kUSD)"
         }
        },
        "yaxis": {
         "title": {
          "text": ""
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "\n",
       "## 3. Key Takeaways & Next Steps\n",
       "\n",
       "The financial analysis strongly supports the project.\n",
       "\n",
       "### Key Takeaways\n",
       "\n",
       "1.  **High Profitability:** The NPV of **$742.01 kUSD** confirms the project's ability to create value significantly above the cost of capital.\n",
       "2.  **Risk Robustness:** The **15.05% IRR premium** provides a strong financial buffer against unforeseen execution risks or adverse market changes.\n",
       "3.  **Early De-Risking:** Value is front-loaded, with the High Growth phase contributing the most to the total PV.\n",
       "\n",
       "### Future Focus\n",
       "\n",
       "| Action | Rationale |\n",
       "|:---|:---|\n",
       "| **Sensitivity Analysis** | Test the impact of a rising Cost of Capital on the NPV threshold. |\n",
       "| **Contingency Planning** | Develop strategies to sustain cash flows in the later Decline phase (Years 7-10). |\n",
       "| **Capital Allocation** | Confirm funding availability for the initial **$1,000 kUSD** investment. |\n"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "import plotly.graph_objects as go\n",
    "from IPython.display import display, Markdown\n",
    "# Import numpy_financial for robust financial calculations (best practice)\n",
    "import numpy_financial as npf\n",
    "\n",
    "# --- Global Data and Configuration ---\n",
    "\n",
    "# Brilliant Blues Palette for Visualization\n",
    "COLORS = ['#003F63', '#006094', '#0088C8', '#30AADD', '#78D0ED']\n",
    "\n",
    "# 10-Year Cash Flow Data (Synthetic, matching infographic) - Values in kUSD\n",
    "CASH_FLOWS = [\n",
    "    -1000, 250, 350, 400, 300, 300, 250, 200, 150, 100, 50\n",
    "]\n",
    "YEARS = list(range(len(CASH_FLOWS))) # Years 0 to 10 (11 total entries)\n",
    "df_cf = pd.DataFrame({'Year': YEARS, 'Cash_Flow': CASH_FLOWS})\n",
    "\n",
    "# Phase Value Data (Present Value Contribution - PV) - Values in kUSD\n",
    "df_phase = pd.DataFrame({\n",
    "    'Phase': ['High Growth (Y 1-3)', 'Maturity (Y 4-6)', 'Decline (Y 7-10)'],\n",
    "    'PV_Contribution': [817.06, 532.30, 234.29] # NOTE: This synthetic data remains hardcoded\n",
    "})\n",
    "\n",
    "# Required rate of return (Discount Rate) as a decimal\n",
    "DISCOUNT_RATE = 0.10\n",
    "\n",
    "# CALCULATE NPV, IRR, AND MARGIN OF SAFETY DYNAMICALLY\n",
    "npv_result = npf.npv(DISCOUNT_RATE, CASH_FLOWS[1:]) + CASH_FLOWS[0]\n",
    "irr_result = npf.irr(CASH_FLOWS)\n",
    "\n",
    "# Convert results to desired display format (percentage/kUSD)\n",
    "npv_kusd = npv_result\n",
    "irr_percent = irr_result*100\n",
    "hurdle_percent = DISCOUNT_RATE*100\n",
    "margin_of_safety_percent=irr_percent-hurdle_percent\n",
    "\n",
    "# --- Function Definitions for Plotly Visualizations ---\n",
    "\n",
    "def create_irr_donut(irr_percent, hurdle_percent):\n",
    "    \"\"\"Generates a donut chart comparing IRR to the Hurdle Rate (Margin of Safety).\"\"\"\n",
    "    \n",
    "    # Convert to decimals for calculation\n",
    "    irr = irr_percent/100\n",
    "    hurdle = hurdle_percent/100\n",
    "    premium = irr-hurdle\n",
    "\n",
    "    # Data for the donut chart\n",
    "    data = pd.DataFrame({\n",
    "        'Label': [f'IRR Premium ({premium:.2%})', f'Hurdle Rate ({hurdle:.2%})'],\n",
    "        'Value': [premium, hurdle]\n",
    "    })\n",
    "\n",
    "    fig = go.Figure(data=[\n",
    "        go.Pie(\n",
    "            labels=data['Label'], \n",
    "            values=data['Value'], \n",
    "            hole=0.6,\n",
    "            marker_colors=[COLORS[2], COLORS[4]],\n",
    "            name=\"\",\n",
    "            hovertemplate = '%{label}<br>Value: %{percent}<extra></extra>'\n",
    "        )\n",
    "    ])\n",
    "\n",
    "    fig.update_layout(\n",
    "        title_text='IRR vs. Hurdle Rate: Margin of Safety',\n",
    "        title_x=0.5,\n",
    "        annotations=[dict(text=f'{irr_percent:.2f}%<br>IRR', x=0.5, y=0.5, font_size=20, showarrow=False)],\n",
    "        template=\"plotly_white\",\n",
    "        height=400\n",
    "    )\n",
    "    fig.show()\n",
    "\n",
    "def create_cash_flow_bar(df):\n",
    "    \"\"\"Generates a bar chart visualizing 10-Year Cash Flows.\"\"\"\n",
    "    \n",
    "    fig = go.Figure()\n",
    "    fig.add_trace(go.Bar(\n",
    "        x=df['Year'], \n",
    "        y=df['Cash_Flow'], \n",
    "        # Color negative (Year 0 investment) flows differently\n",
    "        marker_color=[COLORS[0] if cf < 0 else COLORS[2] for cf in df['Cash_Flow']],\n",
    "        hovertemplate = 'Year %{x}<br>Cash Flow: $%{y:,.0f} kUSD<extra></extra>'\n",
    "    ))\n",
    "\n",
    "    fig.update_layout(\n",
    "        title='Project Alpha: 10-Year Cash Flow Lifecycle',\n",
    "        xaxis_title='Project Year',\n",
    "        yaxis_title='Cash Flow ($ kUSD)',\n",
    "        template=\"plotly_white\",\n",
    "        height=500\n",
    "    )\n",
    "    fig.show()\n",
    "\n",
    "def create_phase_stack_bar(df):\n",
    "    \"\"\"Generates a horizontal stacked bar chart showing PV contribution by phase.\"\"\"\n",
    "\n",
    "    # Create a list of bar traces, one for each phase\n",
    "    traces = [\n",
    "        go.Bar(\n",
    "            name=phase, \n",
    "            y=['PV Contribution'], \n",
    "            x=[value], \n",
    "            orientation='h',\n",
    "            marker_color=COLORS[i],\n",
    "            hovertemplate = f'{phase}: ${{x:,.2f}} kUSD<extra></extra>'\n",
    "        )\n",
    "        for i, (phase, value) in enumerate(zip(df['Phase'], df['PV_Contribution']))\n",
    "    ]\n",
    "    \n",
    "    fig = go.Figure(data=traces)\n",
    "\n",
    "    fig.update_layout(\n",
    "        barmode='stack',\n",
    "        title='Value Deconstruction: PV Contribution by Project Phase',\n",
    "        xaxis_title='Present Value ($ kUSD)',\n",
    "        yaxis_title='',\n",
    "        template=\"plotly_white\",\n",
    "        height=300,\n",
    "        # FIX: Removed unnecessary backslashes (\\\\) from dictionary keys\n",
    "        legend=dict(orientation='h', yanchor='bottom', y=-0.3, xanchor='center', x=0.5)\n",
    "    )\n",
    "    fig.show()\n",
    "\n",
    "# --- Notebook Execution Flow ---\n",
    "\n",
    "# 1. Display Introduction and Metrics Table (equivalent to Markdown Cell 1)\n",
    "# UPDATED: Using f-string for dynamic metrics\n",
    "markdown_intro = f\"\"\"\n",
    "# Project Alpha: A Data Visualization Infographic\n",
    "\n",
    "## **Recommendation: {'ACCEPT' if npv_kusd > 0 else 'REJECT'}**\n",
    "\n",
    "This report visualizes the key financial metrics and forecasts for **Project Alpha**, confirming its viability. The project delivers substantial value, evidenced by a high Net Present Value (NPV) and a significant Internal Rate of Return (IRR) that far exceeds the Hurdle Rate (Cost of Capital). \n",
    "\n",
    "---\n",
    "### Core Financial Metrics (Based on {hurdle_percent:.2f}% Hurdle Rate)\n",
    "\n",
    "| Metric | Value | Conclusion |\n",
    "|:---|:---|:---|\n",
    "| **Net Present Value (NPV)** | **${npv_kusd:,.2f} kUSD** | Expected value generated (NPV {'< 0' if npv_kusd < 0 else '> 0'}) |\n",
    "| **Internal Rate of Return (IRR)** | **{irr_percent:.2f}%** | Project return exceeds required return |\n",
    "| **Hurdle Rate (Cost of Capital)** | **{hurdle_percent:.2f}%** | Benchmark for investment |\n",
    "| **Margin of Safety** | **{margin_of_safety_percent:.2f}%** | Robust buffer against risk |\n",
    "\n",
    "---\n",
    "The analysis below deconstructs the 'why' behind this recommendation, focusing on the project's profitability and lifecycle.\n",
    "\"\"\"\n",
    "display(Markdown(markdown_intro))\n",
    "\n",
    "# 2. Margin of Safety Analysis (equivalent to Code Cell 3)\n",
    "display(Markdown(\"## 1. Margin of Safety Analysis\"))\n",
    "display(Markdown(f\"The **{irr_percent:.2f}% IRR** provides a {margin_of_safety_percent:.2f} percentage point premium over the **{hurdle_percent:.2f}% cost of capital**, demonstrating a strong capacity to absorb risk and maintain profitability. This margin is the foundation of the 'ACCEPT' recommendation.\"))\n",
    "\n",
    "# UPDATED: Calling with dynamic calculated variables\n",
    "create_irr_donut(irr_percent, hurdle_percent)\n",
    "\n",
    "# 3. Project Lifecycle & Value Contribution (equivalent to Code Cell 4)\n",
    "display(Markdown(\"## 2. Project Lifecycle & Value Contribution\"))\n",
    "display(Markdown(\"The initial investment (Year 0) is followed by a predictable pattern of returns, peaking in the High Growth phase (Years 1-3) and stabilizing in the Maturity phase (Years 4-6) before a planned wind-down.\"))\n",
    "\n",
    "create_cash_flow_bar(df_cf)\n",
    "\n",
    "display(Markdown(\"### Value Breakdown by Phase\"))\n",
    "display(Markdown(\"The project's value isn't uniform. The **High Growth** phase creates the most significant portion of the total positive present value, rapidly de-risking the initial investment.\"))\n",
    "\n",
    "create_phase_stack_bar(df_phase)\n",
    "\n",
    "# 4. Key Takeaways & Next Steps (equivalent to Markdown Cell 5)\n",
    "# UPDATED: Using f-string for dynamic metrics\n",
    "markdown_conclusion = f\"\"\"\n",
    "## 3. Key Takeaways & Next Steps\n",
    "\n",
    "The financial analysis strongly supports the project.\n",
    "\n",
    "### Key Takeaways\n",
    "\n",
    "1.  **High Profitability:** The NPV of **${npv_kusd:,.2f} kUSD** confirms the project's ability to create value significantly above the cost of capital.\n",
    "2.  **Risk Robustness:** The **{margin_of_safety_percent:.2f}% IRR premium** provides a strong financial buffer against unforeseen execution risks or adverse market changes.\n",
    "3.  **Early De-Risking:** Value is front-loaded, with the High Growth phase contributing the most to the total PV.\n",
    "\n",
    "### Future Focus\n",
    "\n",
    "| Action | Rationale |\n",
    "|:---|:---|\n",
    "| **Sensitivity Analysis** | Test the impact of a rising Cost of Capital on the NPV threshold. |\n",
    "| **Contingency Planning** | Develop strategies to sustain cash flows in the later Decline phase (Years 7-10). |\n",
    "| **Capital Allocation** | Confirm funding availability for the initial **${-CASH_FLOWS[0]:,.0f} kUSD** investment. |\n",
    "\"\"\"\n",
    "display(Markdown(markdown_conclusion))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "c799443c-2b0b-49af-a966-1ba75e15a897",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "\n",
       "# Project Alpha: A Data Visualization Infographic\n",
       "\n",
       "## **Recommendation: ACCEPT**\n",
       "\n",
       "This report visualizes the key financial metrics and forecasts for **Project Alpha**, confirming its viability. The project delivers substantial value, evidenced by a high Net Present Value (NPV) and a significant Internal Rate of Return (IRR) that far exceeds the Hurdle Rate (Cost of Capital). \n",
       "\n",
       "---\n",
       "### Core Financial Metrics (Based on 10.00% Hurdle Rate)\n",
       "\n",
       "| Metric | Value | Conclusion |\n",
       "|:---|:---|:---|\n",
       "| **Net Present Value (NPV)** | **$742.01 kUSD** | Expected value generated (NPV > 0) |\n",
       "| **Internal Rate of Return (IRR)** | **25.05%** | Project return exceeds required return |\n",
       "| **Hurdle Rate (Cost of Capital)** | **10.00%** | Benchmark for investment |\n",
       "| **Margin of Safety** | **15.05%** | Robust buffer against risk |\n",
       "| **Payback Period** | **4.00 Years** | Fast return of capital (Lower is better) |\n",
       "\n",
       "---\n",
       "The analysis below deconstructs the 'why' behind this recommendation, focusing on the project's profitability and lifecycle.\n"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "## 1. Margin of Safety Analysis"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "The **25.05% IRR** provides a 15.05 percentage point premium over the **10.00% cost of capital**, demonstrating a strong capacity to absorb risk and maintain profitability. This margin is the foundation of the 'ACCEPT' recommendation."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hole": 0.6,
         "hovertemplate": "%{label}<br>Value: %{percent}<extra></extra>",
         "labels": [
          "IRR Premium (15.05%)",
          "Hurdle Rate (10.00%)"
         ],
         "marker": {
          "colors": [
           "#0088C8",
           "#78D0ED"
          ]
         },
         "name": "",
         "type": "pie",
         "values": {
          "bdata": "yz67h8tEwz+amZmZmZm5Pw==",
          "dtype": "f8"
         }
        }
       ],
       "layout": {
        "annotations": [
         {
          "font": {
           "size": 20
          },
          "showarrow": false,
          "text": "25.05%<br>IRR",
          "x": 0.5,
          "y": 0.5
         }
        ],
        "height": 400,
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "white",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "white",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "#C8D4E3",
             "linecolor": "#C8D4E3",
             "minorgridcolor": "#C8D4E3",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "#C8D4E3",
             "linecolor": "#C8D4E3",
             "minorgridcolor": "#C8D4E3",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermap": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermap"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "white",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "#C8D4E3"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "white",
          "polar": {
           "angularaxis": {
            "gridcolor": "#EBF0F8",
            "linecolor": "#EBF0F8",
            "ticks": ""
           },
           "bgcolor": "white",
           "radialaxis": {
            "gridcolor": "#EBF0F8",
            "linecolor": "#EBF0F8",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           },
           "yaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           },
           "zaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           },
           "bgcolor": "white",
           "caxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "#EBF0F8",
           "linecolor": "#EBF0F8",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#EBF0F8",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "#EBF0F8",
           "linecolor": "#EBF0F8",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#EBF0F8",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "IRR vs. Hurdle Rate: Margin of Safety",
         "x": 0.5
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "## 2. Project Lifecycle & Value Contribution"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "The initial investment (Year 0) is followed by a predictable pattern of returns, peaking in the High Growth phase (Years 1-3) and stabilizing in the Maturity phase (Years 4-6) before a planned wind-down."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "Year %{x}<br>Cash Flow: $%{y:,.0f} kUSD<extra></extra>",
         "marker": {
          "color": [
           "#003F63",
           "#0088C8",
           "#0088C8",
           "#0088C8",
           "#0088C8",
           "#0088C8",
           "#0088C8",
           "#0088C8",
           "#0088C8",
           "#0088C8",
           "#0088C8"
          ]
         },
         "type": "bar",
         "x": {
          "bdata": "AAECAwQFBgcICQo=",
          "dtype": "i1"
         },
         "y": {
          "bdata": "GPz6AF4BkAEsASwB+gDIAJYAZAAyAA==",
          "dtype": "i2"
         }
        }
       ],
       "layout": {
        "height": 500,
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "white",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "white",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "#C8D4E3",
             "linecolor": "#C8D4E3",
             "minorgridcolor": "#C8D4E3",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "#C8D4E3",
             "linecolor": "#C8D4E3",
             "minorgridcolor": "#C8D4E3",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermap": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermap"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "white",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "#C8D4E3"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "white",
          "polar": {
           "angularaxis": {
            "gridcolor": "#EBF0F8",
            "linecolor": "#EBF0F8",
            "ticks": ""
           },
           "bgcolor": "white",
           "radialaxis": {
            "gridcolor": "#EBF0F8",
            "linecolor": "#EBF0F8",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           },
           "yaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           },
           "zaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           },
           "bgcolor": "white",
           "caxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "#EBF0F8",
           "linecolor": "#EBF0F8",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#EBF0F8",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "#EBF0F8",
           "linecolor": "#EBF0F8",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#EBF0F8",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Project Alpha: 10-Year Cash Flow Lifecycle"
        },
        "xaxis": {
         "title": {
          "text": "Project Year"
         }
        },
        "yaxis": {
         "title": {
          "text": "Cash Flow ($ kUSD)"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "### Value Breakdown by Phase"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "The project's value isn't uniform. The **High Growth** phase creates the most significant portion of the total positive present value, rapidly de-risking the initial investment."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "High Growth (Y 1-3): ${x:,.2f} kUSD<extra></extra>",
         "marker": {
          "color": "#003F63"
         },
         "name": "High Growth (Y 1-3)",
         "orientation": "h",
         "type": "bar",
         "x": [
          817.06
         ],
         "y": [
          "PV Contribution"
         ]
        },
        {
         "hovertemplate": "Maturity (Y 4-6): ${x:,.2f} kUSD<extra></extra>",
         "marker": {
          "color": "#006094"
         },
         "name": "Maturity (Y 4-6)",
         "orientation": "h",
         "type": "bar",
         "x": [
          532.3
         ],
         "y": [
          "PV Contribution"
         ]
        },
        {
         "hovertemplate": "Decline (Y 7-10): ${x:,.2f} kUSD<extra></extra>",
         "marker": {
          "color": "#0088C8"
         },
         "name": "Decline (Y 7-10)",
         "orientation": "h",
         "type": "bar",
         "x": [
          234.29
         ],
         "y": [
          "PV Contribution"
         ]
        }
       ],
       "layout": {
        "barmode": "stack",
        "height": 300,
        "legend": {
         "orientation": "h",
         "x": 0.5,
         "xanchor": "center",
         "y": -0.3,
         "yanchor": "bottom"
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "white",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "white",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "#C8D4E3",
             "linecolor": "#C8D4E3",
             "minorgridcolor": "#C8D4E3",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "#C8D4E3",
             "linecolor": "#C8D4E3",
             "minorgridcolor": "#C8D4E3",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermap": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermap"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "white",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "#C8D4E3"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "white",
          "polar": {
           "angularaxis": {
            "gridcolor": "#EBF0F8",
            "linecolor": "#EBF0F8",
            "ticks": ""
           },
           "bgcolor": "white",
           "radialaxis": {
            "gridcolor": "#EBF0F8",
            "linecolor": "#EBF0F8",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           },
           "yaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           },
           "zaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           },
           "bgcolor": "white",
           "caxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "#EBF0F8",
           "linecolor": "#EBF0F8",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#EBF0F8",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "#EBF0F8",
           "linecolor": "#EBF0F8",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#EBF0F8",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Value Deconstruction: PV Contribution by Project Phase"
        },
        "xaxis": {
         "title": {
          "text": "Present Value ($ kUSD)"
         }
        },
        "yaxis": {
         "title": {
          "text": ""
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "---"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "## 3. Risk Analysis: NPV Sensitivity Profile"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "The NPV Profile visually confirms the project's robustness. The chart shows that the project remains profitable (NPV > 0) even if the Cost of Capital rises significantly, only becoming unprofitable if the rate exceeds the **IRR of 25.05%**."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "Rate: %{x:.2f}%<br>NPV: $%{y:,.0f} kUSD<extra></extra>",
         "line": {
          "color": "#003F63",
          "width": 3
         },
         "mode": "lines",
         "name": "NPV Profile",
         "type": "scatter",
         "x": {
          "bdata": "AAAAAAAA8D9P2VAmaEP4P0/ZUCZoQwBA9kV5ORxlBECesqFM0IYIQEYfyl+EqAxA90V5ORxlEEBLfA1D9nUSQJ+yoUzQhhRA8+g1VqqXFkBHH8pfhKgYQJtVXmleuRpA7YvycjjKHEBBwoZ8EtseQEp8DUP2dSBAdJfXR2N+IUCesqFM0IYiQMjNa1E9jyNA8ug1VqqXJEAcBABbF6AlQEYfyl+EqCZAcDqUZPGwJ0CaVV5pXrkoQMVwKG7LwSlA7ovycjjKKkAZp7x3pdIrQELChnwS2yxAbd1QgX/jLUCW+BqG7OsuQMET5YpZ9C9AdZfXR2N+MEAKpTzKmQIxQJ+yoUzQhjFANMAGzwYLMkDJzWtRPY8yQF7b0NNzEzNA8+g1VqqXM0CI9prY4Bs0QB0EAFsXoDRAsRFl3U0kNUBHH8pfhKg1QNssL+K6LDZAcTqUZPGwNkAFSPnmJzU3QJtVXmleuTdAL2PD65Q9OEDFcChuy8E4QFl+jfABRjlA7ovycjjKOUCDmVf1bk46QA==",
          "dtype": "f8"
         },
         "y": {
          "bdata": "UhEaqH3hk0CanfcORkiTQCZdmwats5JAsFf5woQjkkAG+gqToZeRQKBDisTZD5FAAqVTiQWMkEDQf1Pe/guQQL4yzOdCH49AvBslL5UtjkAy2xU+skKNQCJWuqhaXoxAWMaDxlGAi0BUne6OXaiKQNK7L3hG1olAiDC6V9cJiUDOvoBE3UKIQC5S2HongYdANkjiQYfEhkDqHWfSzwyGQPySCz/WWYVAosHLXXGrhEDM+aiyeQGEQPJpeFvJW4NAuMPB/Du6gkAeG56vrhyCQIo9iPD/goFA5qkQjw/tgECcMGievlqAQPQeas3el39A9DxOrgqBfkC8qYDxyXB9QJQtj8PnZnxAlK24UzFje0AgVES9dWV6QKDs9/GFbXlA2L+dpTR7eEDwLos6Vo53QPQoGq/ApnZAeGoIjEvEdUAMObDTz+Z0QKAFD/InDnRA7AyPrS86c0DUrIkYxGpyQOS/eIPDn3FABNvNbw3ZcEBg0WaDghZwQGi5LvkIsG5AuICATew6bUDoU9meds1rQA==",
          "dtype": "f8"
         }
        },
        {
         "hovertemplate": "IRR: 25.05%<extra></extra>",
         "marker": {
          "color": "red",
          "size": 10
         },
         "mode": "markers",
         "name": "IRR Point",
         "type": "scatter",
         "x": [
          25.05369580031498
         ],
         "y": [
          0
         ]
        },
        {
         "hovertemplate": "Hurdle Rate: 10.00%<br>NPV: $%742.01 kUSD<extra></extra>",
         "marker": {
          "color": "#30AADD",
          "size": 10
         },
         "mode": "markers",
         "name": "Hurdle Rate NPV",
         "type": "scatter",
         "x": [
          10
         ],
         "y": [
          742.0132609082543
         ]
        }
       ],
       "layout": {
        "height": 500,
        "shapes": [
         {
          "line": {
           "color": "black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 1,
          "x1": 26.30638059033073,
          "y0": 0,
          "y1": 0
         }
        ],
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "white",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "white",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "#C8D4E3",
             "linecolor": "#C8D4E3",
             "minorgridcolor": "#C8D4E3",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "#C8D4E3",
             "linecolor": "#C8D4E3",
             "minorgridcolor": "#C8D4E3",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermap": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermap"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "white",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "#C8D4E3"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "white",
          "polar": {
           "angularaxis": {
            "gridcolor": "#EBF0F8",
            "linecolor": "#EBF0F8",
            "ticks": ""
           },
           "bgcolor": "white",
           "radialaxis": {
            "gridcolor": "#EBF0F8",
            "linecolor": "#EBF0F8",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           },
           "yaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           },
           "zaxis": {
            "backgroundcolor": "white",
            "gridcolor": "#DFE8F3",
            "gridwidth": 2,
            "linecolor": "#EBF0F8",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#EBF0F8"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           },
           "bgcolor": "white",
           "caxis": {
            "gridcolor": "#DFE8F3",
            "linecolor": "#A2B1C6",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "#EBF0F8",
           "linecolor": "#EBF0F8",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#EBF0F8",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "#EBF0F8",
           "linecolor": "#EBF0F8",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#EBF0F8",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "NPV Sensitivity Analysis (NPV Profile)"
        },
        "xaxis": {
         "title": {
          "text": "Discount Rate (%)"
         }
        },
        "yaxis": {
         "title": {
          "text": "Net Present Value ($ kUSD)"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "\n",
       "## 4. Key Takeaways & Next Steps\n",
       "\n",
       "The financial analysis strongly supports the project.\n",
       "\n",
       "### Key Takeaways\n",
       "\n",
       "1.  **High Profitability:** The NPV of **$742.01 kUSD** confirms the project's ability to create value significantly above the cost of capital.\n",
       "2.  **Risk Robustness:** The **15.05% IRR premium** provides a strong financial buffer against unforeseen execution risks or adverse market changes.\n",
       "3.  **Liquidity:** The **4.00-year Payback Period** indicates a fast return of capital.\n",
       "4.  **Sensitivity:** The project is resilient, with a wide gap between the current 10.00% Hurdle Rate and the 25.05% IRR threshold.\n",
       "\n",
       "### Future Focus\n",
       "\n",
       "| Action | Rationale |\n",
       "|:---|:---|\n",
       "| **Sensitivity Analysis** | Perform a sensitivity test on the primary revenue stream (Cash Flow) to see the minimum acceptable cash flow. |\n",
       "| **Contingency Planning** | Develop strategies to sustain cash flows in the later Decline phase (Years 7-10). |\n",
       "| **Capital Allocation** | Confirm funding availability for the initial **$1,000 kUSD** investment. |\n"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#updating project_alpha_infographic.py to include a dynamic Payback Period calculation and a Plotly chart for NPV Sensitivity.\n",
    "\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "import plotly.graph_objects as go\n",
    "from IPython.display import display, Markdown\n",
    "# Import numpy_financial for robust financial calculations (best practice)\n",
    "import numpy_financial as npf\n",
    "\n",
    "# --- Global Data and Configuration ---\n",
    "\n",
    "# Brilliant Blues Palette for Visualization\n",
    "COLORS = ['#003F63', '#006094', '#0088C8', '#30AADD', '#78D0ED']\n",
    "\n",
    "# 10-Year Cash Flow Data (Synthetic, matching infographic) - Values in kUSD\n",
    "CASH_FLOWS = np.array([ # Use numpy array for easier cumulative sums\n",
    "    -1000, 250, 350, 400, 300, 300, 250, 200, 150, 100, 50\n",
    "])\n",
    "YEARS = list(range(len(CASH_FLOWS))) # Years 0 to 10 (11 total entries)\n",
    "df_cf = pd.DataFrame({'Year': YEARS, 'Cash_Flow': CASH_FLOWS})\n",
    "\n",
    "# Phase Value Data (Present Value Contribution - PV) - Values in kUSD\n",
    "df_phase = pd.DataFrame({\n",
    "    'Phase': ['High Growth (Y 1-3)', 'Maturity (Y 4-6)', 'Decline (Y 7-10)'],\n",
    "    'PV_Contribution': [817.06, 532.30, 234.29] # NOTE: This synthetic data remains hardcoded\n",
    "})\n",
    "\n",
    "# Required rate of return (Discount Rate) as a decimal\n",
    "DISCOUNT_RATE = 0.10\n",
    "\n",
    "# --- Financial Calculation Functions ---\n",
    "\n",
    "def calculate_payback_period(cash_flows):\n",
    "    \"\"\"Calculates the Payback Period in years.\"\"\"\n",
    "    cumulative_cf = np.cumsum(cash_flows)\n",
    "    \n",
    "    # Find the last year where cumulative CF is negative\n",
    "    payback_year_index = np.where(cumulative_cf < 0)[0]\n",
    "    \n",
    "    if len(payback_year_index) == len(cash_flows):\n",
    "        return np.nan # Never pays back\n",
    "    \n",
    "    if len(payback_year_index) == 0:\n",
    "        return 0 # Pays back in Year 0 (or immediately)\n",
    "\n",
    "    last_negative_year = payback_year_index[-1]\n",
    "    \n",
    "    # The absolute value of the remaining investment needed\n",
    "    remaining_investment = abs(cumulative_cf[last_negative_year])\n",
    "    \n",
    "    # Cash flow in the next year (recovery year)\n",
    "    cash_flow_in_recovery_year = cash_flows[last_negative_year + 1]\n",
    "    \n",
    "    # Fractional part of the recovery year\n",
    "    fractional_year = remaining_investment / cash_flow_in_recovery_year\n",
    "    \n",
    "    return last_negative_year + 1 + fractional_year\n",
    "\n",
    "\n",
    "# --- DYNAMIC METRICS CALCULATION ---\n",
    "\n",
    "npv_result = npf.npv(DISCOUNT_RATE, CASH_FLOWS[1:]) + CASH_FLOWS[0]\n",
    "irr_result = npf.irr(CASH_FLOWS)\n",
    "payback_result = calculate_payback_period(CASH_FLOWS)\n",
    "\n",
    "# Convert results to desired display format (percentage/kUSD)\n",
    "npv_kusd = npv_result\n",
    "irr_percent = irr_result * 100\n",
    "hurdle_percent = DISCOUNT_RATE * 100\n",
    "margin_of_safety_percent = irr_percent - hurdle_percent\n",
    "\n",
    "\n",
    "# --- Function Definitions for Plotly Visualizations ---\n",
    "\n",
    "def create_irr_donut(irr_percent, hurdle_percent):\n",
    "    \"\"\"Generates a donut chart comparing IRR to the Hurdle Rate (Margin of Safety).\"\"\"\n",
    "    \n",
    "    # Convert to decimals for calculation\n",
    "    irr = irr_percent / 100\n",
    "    hurdle = hurdle_percent / 100\n",
    "    premium = irr - hurdle\n",
    "\n",
    "    # Data for the donut chart\n",
    "    data = pd.DataFrame({\n",
    "        'Label': [f'IRR Premium ({premium:.2%})', f'Hurdle Rate ({hurdle:.2%})'],\n",
    "        'Value': [premium, hurdle]\n",
    "    })\n",
    "\n",
    "    fig = go.Figure(data=[\n",
    "        go.Pie(\n",
    "            labels=data['Label'], \n",
    "            values=data['Value'], \n",
    "            hole=0.6,\n",
    "            marker_colors=[COLORS[2], COLORS[4]],\n",
    "            name=\"\",\n",
    "            hovertemplate = '%{label}<br>Value: %{percent}<extra></extra>'\n",
    "        )\n",
    "    ])\n",
    "\n",
    "    fig.update_layout(\n",
    "        title_text='IRR vs. Hurdle Rate: Margin of Safety',\n",
    "        title_x=0.5,\n",
    "        annotations=[dict(text=f'{irr_percent:.2f}%<br>IRR', x=0.5, y=0.5, font_size=20, showarrow=False)],\n",
    "        template=\"plotly_white\",\n",
    "        height=400\n",
    "    )\n",
    "    fig.show()\n",
    "\n",
    "def create_cash_flow_bar(df):\n",
    "    \"\"\"Generates a bar chart visualizing 10-Year Cash Flows.\"\"\"\n",
    "    \n",
    "    fig = go.Figure()\n",
    "    fig.add_trace(go.Bar(\n",
    "        x=df['Year'], \n",
    "        y=df['Cash_Flow'], \n",
    "        # Color negative (Year 0 investment) flows differently\n",
    "        marker_color=[COLORS[0] if cf < 0 else COLORS[2] for cf in df['Cash_Flow']],\n",
    "        hovertemplate = 'Year %{x}<br>Cash Flow: $%{y:,.0f} kUSD<extra></extra>'\n",
    "    ))\n",
    "\n",
    "    fig.update_layout(\n",
    "        title='Project Alpha: 10-Year Cash Flow Lifecycle',\n",
    "        xaxis_title='Project Year',\n",
    "        yaxis_title='Cash Flow ($ kUSD)',\n",
    "        template=\"plotly_white\",\n",
    "        height=500\n",
    "    )\n",
    "    fig.show()\n",
    "\n",
    "def create_phase_stack_bar(df):\n",
    "    \"\"\"Generates a horizontal stacked bar chart showing PV contribution by phase.\"\"\"\n",
    "    \n",
    "    # Create a list of bar traces, one for each phase\n",
    "    traces = [\n",
    "        go.Bar(\n",
    "            name=phase, \n",
    "            y=['PV Contribution'], \n",
    "            x=[value], \n",
    "            orientation='h',\n",
    "            marker_color=COLORS[i],\n",
    "            hovertemplate = f'{phase}: ${{x:,.2f}} kUSD<extra></extra>'\n",
    "        )\n",
    "        for i, (phase, value) in enumerate(zip(df['Phase'], df['PV_Contribution']))\n",
    "    ]\n",
    "    \n",
    "    fig = go.Figure(data=traces)\n",
    "\n",
    "    fig.update_layout(\n",
    "        barmode='stack',\n",
    "        title='Value Deconstruction: PV Contribution by Project Phase',\n",
    "        xaxis_title='Present Value ($ kUSD)',\n",
    "        yaxis_title='',\n",
    "        template=\"plotly_white\",\n",
    "        height=300,\n",
    "        legend=dict(orientation='h', yanchor='bottom', y=-0.3, xanchor='center', x=0.5)\n",
    "    )\n",
    "    fig.show()\n",
    "\n",
    "\n",
    "def create_npv_sensitivity_chart(cash_flows, irr_result, hurdle_percent):\n",
    "    \"\"\"Generates the NPV Profile Chart showing sensitivity to the Discount Rate.\"\"\"\n",
    "    \n",
    "    # Define a range of discount rates from 0% to IRR + 5%\n",
    "    max_rate = max(irr_result * 1.05, 0.25)\n",
    "    rates = np.linspace(0.01, max_rate, 50)\n",
    "    \n",
    "    # Calculate NPV for each rate\n",
    "    npvs = [npf.npv(rate, cash_flows[1:]) + cash_flows[0] for rate in rates]\n",
    "    \n",
    "    df_sensitivity = pd.DataFrame({\n",
    "        'Discount_Rate': rates * 100, # Convert to percentage for display\n",
    "        'NPV': npvs\n",
    "    })\n",
    "    \n",
    "    fig = go.Figure()\n",
    "    \n",
    "    # 1. NPV Profile Line\n",
    "    fig.add_trace(go.Scatter(\n",
    "        x=df_sensitivity['Discount_Rate'],\n",
    "        y=df_sensitivity['NPV'],\n",
    "        mode='lines',\n",
    "        name='NPV Profile',\n",
    "        line=dict(color=COLORS[0], width=3),\n",
    "        hovertemplate='Rate: %{x:.2f}%<br>NPV: $%{y:,.0f} kUSD<extra></extra>'\n",
    "    ))\n",
    "    \n",
    "    # 2. IRR Marker (Zero-crossing point)\n",
    "    fig.add_trace(go.Scatter(\n",
    "        x=[irr_result * 100],\n",
    "        y=[0],\n",
    "        mode='markers',\n",
    "        name='IRR Point',\n",
    "        marker=dict(size=10, color='red'),\n",
    "        hovertemplate=f'IRR: {irr_result * 100:.2f}%<extra></extra>'\n",
    "    ))\n",
    "\n",
    "    # 3. Hurdle Rate (Discount Rate) Marker\n",
    "    fig.add_trace(go.Scatter(\n",
    "        x=[hurdle_percent],\n",
    "        y=[npf.npv(hurdle_percent / 100, cash_flows[1:]) + cash_flows[0]],\n",
    "        mode='markers',\n",
    "        name='Hurdle Rate NPV',\n",
    "        marker=dict(size=10, color=COLORS[3]),\n",
    "        hovertemplate=f'Hurdle Rate: {hurdle_percent:.2f}%<br>NPV: $%{npv_result:,.2f} kUSD<extra></extra>'\n",
    "    ))\n",
    "    \n",
    "    # Layout and Annotations\n",
    "    fig.update_layout(\n",
    "        title='NPV Sensitivity Analysis (NPV Profile)',\n",
    "        xaxis_title='Discount Rate (%)',\n",
    "        yaxis_title='Net Present Value ($ kUSD)',\n",
    "        template=\"plotly_white\",\n",
    "        height=500,\n",
    "        # Draw Zero NPV line\n",
    "        shapes=[\n",
    "            dict(\n",
    "                type='line',\n",
    "                y0=0, y1=0, x0=df_sensitivity['Discount_Rate'].min(), x1=df_sensitivity['Discount_Rate'].max(),\n",
    "                line=dict(color='black', width=1, dash='dot')\n",
    "            )\n",
    "        ]\n",
    "    )\n",
    "    fig.show()\n",
    "\n",
    "# --- Notebook Execution Flow ---\n",
    "\n",
    "# 1. Display Introduction and Metrics Table (equivalent to Markdown Cell 1)\n",
    "# UPDATED: Added Payback Period to the metrics table\n",
    "markdown_intro = f\"\"\"\n",
    "# Project Alpha: A Data Visualization Infographic\n",
    "\n",
    "## **Recommendation: {'ACCEPT' if npv_kusd > 0 else 'REJECT'}**\n",
    "\n",
    "This report visualizes the key financial metrics and forecasts for **Project Alpha**, confirming its viability. The project delivers substantial value, evidenced by a high Net Present Value (NPV) and a significant Internal Rate of Return (IRR) that far exceeds the Hurdle Rate (Cost of Capital). \n",
    "\n",
    "---\n",
    "### Core Financial Metrics (Based on {hurdle_percent:.2f}% Hurdle Rate)\n",
    "\n",
    "| Metric | Value | Conclusion |\n",
    "|:---|:---|:---|\n",
    "| **Net Present Value (NPV)** | **${npv_kusd:,.2f} kUSD** | Expected value generated (NPV {'< 0' if npv_kusd < 0 else '> 0'}) |\n",
    "| **Internal Rate of Return (IRR)** | **{irr_percent:.2f}%** | Project return exceeds required return |\n",
    "| **Hurdle Rate (Cost of Capital)** | **{hurdle_percent:.2f}%** | Benchmark for investment |\n",
    "| **Margin of Safety** | **{margin_of_safety_percent:.2f}%** | Robust buffer against risk |\n",
    "| **Payback Period** | **{payback_result:.2f} Years** | Fast return of capital (Lower is better) |\n",
    "\n",
    "---\n",
    "The analysis below deconstructs the 'why' behind this recommendation, focusing on the project's profitability and lifecycle.\n",
    "\"\"\"\n",
    "display(Markdown(markdown_intro))\n",
    "\n",
    "# 2. Margin of Safety Analysis (equivalent to Code Cell 3)\n",
    "display(Markdown(\"## 1. Margin of Safety Analysis\"))\n",
    "display(Markdown(f\"The **{irr_percent:.2f}% IRR** provides a {margin_of_safety_percent:.2f} percentage point premium over the **{hurdle_percent:.2f}% cost of capital**, demonstrating a strong capacity to absorb risk and maintain profitability. This margin is the foundation of the 'ACCEPT' recommendation.\"))\n",
    "\n",
    "create_irr_donut(irr_percent, hurdle_percent)\n",
    "\n",
    "# 3. Project Lifecycle & Value Contribution (equivalent to Code Cell 4)\n",
    "display(Markdown(\"## 2. Project Lifecycle & Value Contribution\"))\n",
    "display(Markdown(\"The initial investment (Year 0) is followed by a predictable pattern of returns, peaking in the High Growth phase (Years 1-3) and stabilizing in the Maturity phase (Years 4-6) before a planned wind-down.\"))\n",
    "\n",
    "create_cash_flow_bar(df_cf)\n",
    "\n",
    "display(Markdown(\"### Value Breakdown by Phase\"))\n",
    "display(Markdown(\"The project's value isn't uniform. The **High Growth** phase creates the most significant portion of the total positive present value, rapidly de-risking the initial investment.\"))\n",
    "\n",
    "create_phase_stack_bar(df_phase)\n",
    "\n",
    "\n",
    "# --- NEW SECTION: NPV SENSITIVITY ---\n",
    "display(Markdown(\"---\"))\n",
    "display(Markdown(\"## 3. Risk Analysis: NPV Sensitivity Profile\"))\n",
    "display(Markdown(f\"The NPV Profile visually confirms the project's robustness. The chart shows that the project remains profitable (NPV > 0) even if the Cost of Capital rises significantly, only becoming unprofitable if the rate exceeds the **IRR of {irr_percent:.2f}%**.\"))\n",
    "\n",
    "create_npv_sensitivity_chart(CASH_FLOWS, irr_result, hurdle_percent)\n",
    "\n",
    "\n",
    "# 4. Key Takeaways & Next Steps (equivalent to Markdown Cell 5)\n",
    "# UPDATED: Adjusted section header\n",
    "markdown_conclusion = f\"\"\"\n",
    "## 4. Key Takeaways & Next Steps\n",
    "\n",
    "The financial analysis strongly supports the project.\n",
    "\n",
    "### Key Takeaways\n",
    "\n",
    "1.  **High Profitability:** The NPV of **${npv_kusd:,.2f} kUSD** confirms the project's ability to create value significantly above the cost of capital.\n",
    "2.  **Risk Robustness:** The **{margin_of_safety_percent:.2f}% IRR premium** provides a strong financial buffer against unforeseen execution risks or adverse market changes.\n",
    "3.  **Liquidity:** The **{payback_result:.2f}-year Payback Period** indicates a fast return of capital.\n",
    "4.  **Sensitivity:** The project is resilient, with a wide gap between the current {hurdle_percent:.2f}% Hurdle Rate and the {irr_percent:.2f}% IRR threshold.\n",
    "\n",
    "### Future Focus\n",
    "\n",
    "| Action | Rationale |\n",
    "|:---|:---|\n",
    "| **Sensitivity Analysis** | Perform a sensitivity test on the primary revenue stream (Cash Flow) to see the minimum acceptable cash flow. |\n",
    "| **Contingency Planning** | Develop strategies to sustain cash flows in the later Decline phase (Years 7-10). |\n",
    "| **Capital Allocation** | Confirm funding availability for the initial **${-CASH_FLOWS[0]:,.0f} kUSD** investment. |\n",
    "\"\"\"\n",
    "display(Markdown(markdown_conclusion))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "1f57d46d-b443-4c2e-90b3-c25050be5e62",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--- Initial Data Snapshot ---\n",
      "   Product ID  Sale Price  Cost of Goods  Price Point USD\n",
      "0        1001        50.0           10.0               50\n",
      "1        1002       120.0           40.0              120\n",
      "2        1001        50.0           12.0               50\n",
      "3        1003        25.0            5.0               25\n",
      "4        1002       110.0           35.0              110\n",
      "\n",
      "========================================\n",
      "\n",
      "--- Cleaned Columns ---\n",
      "['transaction_id', 'product_id', 'sale_price', 'cost_of_goods', 'price_point_usd', 'purchase_date']\n",
      "\n",
      "========================================\n",
      "\n",
      "--- Final Aggregated Pricing Data ---\n",
      "   product_id  price_point_usd  total_net_revenue  count_of_transactions\n",
      "0        1001               50              118.0                      3\n",
      "1        1001               55               83.0                      2\n",
      "2        1002              110              150.0                      2\n",
      "3        1002              120              160.0                      2\n",
      "4        1003               25               39.0                      2\n",
      "5        1003               28               22.0                      1\n",
      "6        1004              300              390.0                      2\n",
      "7        1004              310              190.0                      1\n"
     ]
    }
   ],
   "source": [
    "#Data Wrangling & Feature Engineering\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# --- 1. Load the Simulated Data ---\n",
    "# In a real internship, this would be read from a cloud storage or database.\n",
    "# We simulate a messy CSV with various pricing and cost columns.\n",
    "data = {\n",
    "    'Transaction ID': np.arange(100, 115),\n",
    "    'Product ID': [1001, 1002, 1001, 1003, 1002, 1001, 1004, 1003, 1001, 1002, 1004, 1003, 1001, 1004, 1002],\n",
    "    'Sale Price': [50.00, 120.00, 50.00, 25.00, 110.00, 55.00, 300.00, 25.00, 50.00, 120.00, 300.00, 28.00, 55.00, 310.00, 110.00],\n",
    "    'Cost of Goods': [10.00, 40.00, 12.00, 5.00, 35.00, 12.00, 100.00, 6.00, 10.00, 40.00, 110.00, 6.00, 15.00, 120.00, 35.00],\n",
    "    'Price Point USD': [50, 120, 50, 25, 110, 55, 300, 25, 50, 120, 300, 28, 55, 310, 110],\n",
    "    'Purchase Date': pd.to_datetime(['2023-10-01', '2023-10-02', '2023-10-02', '2023-10-03', '2023-10-03', '2023-10-04', '2023-10-04', '2023-10-05', '2023-10-05', '2023-10-06', '2023-10-06', '2023-10-07', '2023-10-07', '2023-10-08', '2023-10-08'])\n",
    "}\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "print(\"--- Initial Data Snapshot ---\")\n",
    "print(df[['Product ID', 'Sale Price', 'Cost of Goods', 'Price Point USD']].head())\n",
    "print(\"\\n\" + \"=\"*40 + \"\\n\")\n",
    "\n",
    "\n",
    "# --- 2. Clean Column Names ---\n",
    "# This is a critical step in a professional environment for consistency\n",
    "df.columns = df.columns.str.lower().str.replace(' ', '_')\n",
    "\n",
    "print(\"--- Cleaned Columns ---\")\n",
    "print(df.columns.tolist())\n",
    "print(\"\\n\" + \"=\"*40 + \"\\n\")\n",
    "\n",
    "\n",
    "# --- 3. Calculate Key Metric: Net Revenue ---\n",
    "# This is a standard feature engineering step\n",
    "df['net_revenue'] = df['sale_price'] - df['cost_of_goods']\n",
    "\n",
    "\n",
    "# --- 4. Aggregate Data for Pricing Elasticity Analysis ---\n",
    "# Group by Product and the specific Price Point to find Volume and Revenue\n",
    "aggregated_df = df.groupby(['product_id', 'price_point_usd']).agg(\n",
    "    total_net_revenue=('net_revenue', 'sum'),\n",
    "    count_of_transactions=('transaction_id', 'count')\n",
    ").reset_index()\n",
    "\n",
    "\n",
    "# --- 5. Output Final Table ---\n",
    "print(\"--- Final Aggregated Pricing Data ---\")\n",
    "# The resulting table is now ready for elasticity modeling (Price vs. Count)\n",
    "print(aggregated_df.sort_values(by=['product_id', 'price_point_usd']))\n",
    "\n",
    "# Interpretation Example (for PL):\n",
    "# Product 1001 was sold at $50 (3 times for $118 net revenue) AND $55 (2 times for $78 net revenue).\n",
    "# This table is the input for the Elasticity Model."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "20e8973a-9eee-4454-8875-b60d0787c871",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nHere are some examples of the quality that we are looking for:\\n\\nhttps://www.datawallet.com/crypto/best-crypto-futures-exchanges\\nhttps://finestel.com/blog/best-crypto-copy-trading-platforms/\\nhttps://coinwire.com/mexc-vs-kucoin/\\n'"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"\n",
    "Writing Requirements\n",
    "\n",
    "Our articles must be well articulated, logical, concise, and coherent.\n",
    "You also need to provide your own opinion, research, and analysis.\n",
    "\n",
    "We don't restrict creativity — quite the opposite.\n",
    "\"\"\"\n",
    "\"\"\"\n",
    "Here are some examples of the quality that we are looking for:\n",
    "\n",
    "https://www.datawallet.com/crypto/best-crypto-futures-exchanges\n",
    "https://finestel.com/blog/best-crypto-copy-trading-platforms/\n",
    "https://coinwire.com/mexc-vs-kucoin/\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca2ed9fd-2d2b-41b9-8046-d5633e21c40f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
