#!/usr/bin/env python3
import logging


def error_log_setup():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    )

    return logging.getLogger(__name__)


def generate_invitations(template, attendees):
    logger = error_log_setup()

    if not isinstance(template, str):
        logger.error("Template is not string")
        return
    if not (isinstance(attendees, list)
            and all(isinstance(attendee, dict)
                    for attendee in attendees)):
        logger.error("Attendees is not a list of dictionaries")
        return

    if len(template) == 0:
        logger.error("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        logger.error("No data provided, no output files generated.")
        return

    invitations = []

    for attendee in attendees:
        invitation = template
        for template_key, data in attendee.items():
            if data is None:
                data = "N/A"
            invitation = invitation.replace("{" + template_key + "}", data)
        invitations.append(invitation)

    i = 1
    for invitation in invitations:
        with open(f"output_{i}.txt", "w", encoding="utf-8") as file:
            file.write(invitation)
        i += 1
