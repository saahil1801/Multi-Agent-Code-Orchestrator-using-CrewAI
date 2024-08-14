  expected_output="""A complete newsletter in markdown format, with a consistent style and layout.
                        Example Output: 
                        '# Top stories in AI today:\\n\\n
                        - AI takes spotlight in Super Bowl commercials\\n
                        - Altman seeks TRILLIONS for global AI chip initiative\\n\\n

                        ## AI takes spotlight in Super Bowl commercials\\n\\n
                        **The Rundown:** AI made a splash in this year\'s Super Bowl commercials...\\n\\n
                        **The details:**...\\n\\n
                        **Why it matters::**...\\n\\n
                        ## Altman seeks TRILLIONS for global AI chip initiative\\n\\n
                        **The Rundown:** OpenAI CEO Sam Altman is reportedly angling to raise TRILLIONS of dollars...\\n\\n'
                        **The details:**...\\n\\n
                        **Why it matters::**...\\n\\n
                    """,
            callback=callback_function