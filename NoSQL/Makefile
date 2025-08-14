up:
	docker compose up -d

down:
	docker compose down -v

run0:
	cat 0-list_databases | docker compose exec -T mongo mongo

run1:
	cat 1-use_or_create_database | docker compose exec -T mongo mongo

run2:
	cat 2-insert | docker compose exec -T mongo mongo my_db

run3:
	cat 3-all | docker compose exec -T mongo mongo my_db

run4:
	cat 4-match | docker compose exec -T mongo mongo my_db

run5:
	cat 5-count | docker compose exec -T mongo mongo my_db

run6:
	cat 6-update | docker compose exec -T mongo mongo my_db

run7:
	cat 7-delete | docker compose exec -T mongo mongo my_db


py8:
	docker compose run --rm py python3 8-main.py

py9:
	docker compose exec -T py python 9-insert_school.py

py10:
	docker compose exec -T py python 10-update_topics.py

py11:
	docker compose exec -T py python 11-schools_by_topic.py

py12:
	docker compose exec -T py python 12-log_stats.py
